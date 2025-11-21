# qa-api-python
Python-based API automation with GitHub Actions CI

![API Tests](https://github.com/salymzhanova/qa-api-python/actions/workflows/ci.yml/badge.svg).

## How to run locally
```bash
python3 -m venv venv
source venv/bin/activate
pip install pytest pytest-playwright
playwright install
pytest
