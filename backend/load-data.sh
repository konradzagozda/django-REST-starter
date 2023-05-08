#!/usr/bin/env bash -ex

export $(cat .env | xargs)

export DB_HOST=localhost
export REDIS_HOST=localhost
export RABBITMQ_HOST=localhost

poetry run python manage.py migrate
poetry run python manage.py load_users
poetry run python manage.py loaddata todos.json
