# Usage

## Installation

    pipenv install

## Starting Virtual Environment

Default environment

    pipenv shell

Using QA environment

    PIPENV_DOTENV_LOCATION=.env.qa pipenv shell

## Running Tests

Single file self-test:

    python src/slack.py

From a submodule:

    PYTHONPATH=src python src/restaurants/mauno.py

Unit tests:

    pytest tests/unit

All tests (including integration tests):

    pytest

Single test:

    pytest tests/unit/test_build_payload.py
