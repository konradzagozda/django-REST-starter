#!/bin/bash -ex

python manage.py load_users
python manage.py loaddata todos.json
