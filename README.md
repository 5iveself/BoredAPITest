# Bored API Test Suite

Automated API test suite for the [Bored API](https://bored-api.appbrewery.com/), built with `pytest` and `requests`.

## What's covered

- **Response validation** — status codes, content type, and response schema for the core endpoints
- **Positive scenarios** — fetching a random activity, filtering by type and participant count, fetching an activity by key
- **Negative scenarios** — requesting a non-existent activity key
- **Parametrized tests** — all activity types and participant counts are tested through `pytest.mark.parametrize`, not copy-pasted test functions

## Tech stack

- Python 3.12
- pytest
- requests
- pydantic-settings (config from `.env`)

## Project structure

```
tests/
├── config.py            # settings loaded from .env
├── conftest.py          # fixtures (client, config)
└── test_rest_api.py     # all test cases: random activity, filters, lookup by key
.env                      # local environment variables (not committed)
.env.example               # required environment variables (no secrets)
requirements.txt
```

## Setup

```bash
git clone https://github.com/keirnad/BoredAPITest.git
cd BoredAPITest
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

## Running the tests

```bash
pytest -v
```

Generate an HTML report:

```bash
pytest -v --html=report.html --self-contained-html
```

## API quirks found during testing

- The `participants` filter is documented inconsistently — the API itself expects the query parameter `participiant` (not `participants`). This is confirmed against the live API and is **not a typo in the test suite**; it's handled intentionally and noted inline in the relevant test.

## Possible next steps

- GitHub Actions CI (run tests + publish the HTML report on every push)
- Response schema validation via Pydantic models instead of per-field `assert "key" in data`
- Split `test_rest_api.py` into separate files per endpoint group as the suite grows