#!/bin/bash -ex

./run-cmd.sh python manage.py load_users
./run-cmd.sh python manage.py loaddata todos.json
