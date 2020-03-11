#!/bin/sh

pipenv install --deploy \
&& pipenv run pytest \
&& pipenv lock -r > requirements.txt \
&& echo requirements.txt updated
