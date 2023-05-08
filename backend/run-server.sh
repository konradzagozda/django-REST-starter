#!/usr/bin/env bash

set -ex

source ./load-env.sh

poetry run python manage.py migrate
poetry run python manage.py runserver
