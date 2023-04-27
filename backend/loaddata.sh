#!/bin/bash -ex

docker compose exec backend python manage.py load_users
docker compose exec backend python manage.py loaddata todos.json
