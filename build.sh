#!/bin/sh

pipenv install --deploy \
&& pipenv run pytest \
&& pipenv lock -r > requirements.txt \
&& echo requirements.txt updated \
&& docker &>/dev/null && docker build -t lunch-slack . || echo docker build not available \
&& echo Ready
