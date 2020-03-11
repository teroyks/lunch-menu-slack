# Lunch Menus to Slack

A script that scrapes today’s lunch menus from web pages and posts them to Slack.

This is created for my personal use, but you’re free to modify and use it for your own needs. (Naturally, you need to write the modules to scrape the restaurants you want yourself, but there are examples in the code.)

## Requirements

- Python 3
- `pipenv` for managing the development environment (although you can do all the things manually without it as well)
- `docker` if you want to package the app with the included build script (optional)

## Installation

Install the development environment with

    pipenv install --dev

## Configuration

See [Configuring your Slack app](docs/configure-slack.md).

## Running the App

### In the Development Environment

Run the app with `pipenv`:

    pipenv run python main.py

By default this uses the `.env` file and does not post anything to Slack. You can define which environment to use at run time, e.g.:

    PIPENV_DOTENV_LOCATION=.qa.env pipenv run python main.py

### With Docker

The build script packages the app into a Docker container if `docker` is available. Pass the environment settings file as an argument when running the app:

    $ ./build.sh
    $ docker run --rm --env-file=.qa.env lunch-slack

### Without Docker (with `virtualenv`)

If you don’t have Docker available, you can still use the build script to generate a `requirements.txt` file, and use [virtualenv](https://docs.python-guide.org/dev/virtualenvs/ "Virtualenv documentation") to build the environment with all the required packages installed.
