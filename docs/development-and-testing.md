# Development and Testing

## Development Environment

You can start a shell in the development environment; this way you don't need to use `pipenv` for every command you use.

    pipenv shell
    python main.py
    python src/slack.py
    # etc.

## Adding New Restaurants

Each restaurant is a module in the [`src/restaurants`](../src/restaurants/) directory. The restaurant list is built automatically, so all you need to do is add a new `.py` file in that directory and the scraper module will find it.

Each restaurant module needs to have a `fetch` function. This function takes no arguments and returns a `Restaurant` object (object content is defined in the [`helpers`](../src/helpers.py) module).

## Testing

### Running Tests

All examples are run in the development shell.

Run unit tests:

    pytest tests/unit

Run integration tests (fetch the real menu content; in the default env do not post anything to Slack):

    pytest tests/integration

Running `pytest` with no arguments runs all the tests. If you add new tests, put them under the unit or integration directory, depending on test type.

You can run a single test with `-k`, for example:

    pytest -k test_build_payload

### Test Fixtures

Unit tests for parsing restaurant data use a fixture: real web page content saved in a file (so running a test doesn’t contact the actual web page).

Creating a fixture in the dev shell:

    $ python
    >>> import pickle
    >>> import requests
    >>> res = requests.get('https://restaurant.example.com/lunch')
    >>> with open('tests/unit/fixtures/example-restaurant.response', 'wb') as f:
    >>>     pickle.dump(res, f)

See [`test_lounaat_info`](../tests/unit/test_lounaat_info.py) for an example.
