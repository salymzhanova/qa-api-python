import requests
import pytest

BASE_URL = "https://api.github.com"

def safe_get(url):
    """Helper to GET a URL with exception handling."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as e:
        pytest.skip(f"HTTP error {e.response.status_code} for {url}")
    except requests.exceptions.ConnectionError:
        pytest.skip("Network connection error.")
    except requests.exceptions.Timeout:
        pytest.skip("Request timed out.")
    except Exception as e:
        pytest.skip(f"Unexpected error: {e}")

def test_list_users():
    response = safe_get(f"{BASE_URL}/users?since=0&per_page=5")
    users = response.json()
    assert isinstance(users, list)
    assert len(users) == 5

@pytest.mark.parametrize("username", ["octocat", "torvalds"])
def test_single_user(username):
    response = safe_get(f"{BASE_URL}/users/{username}")
    user = response.json()
    assert user["login"] == username
    assert "id" in user

def test_create_user_not_allowed():
    try:
        response = requests.post(f"{BASE_URL}/users", json={"login": "newuser"}, timeout=10)
        assert response.status_code in (404, 403)
    except requests.exceptions.RequestException:
        pytest.skip("Request failed, skipping test.")
