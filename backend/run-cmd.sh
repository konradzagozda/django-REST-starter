#!/bin/bash -ex

# run command inside backend container
#
# usage: ./run-cmd.sh <command>
# 	e.g. ./run-cmd.sh pytest -n 8
#
# prerequisite: running stack with "docker compose up"

docker compose exec -it backend "$@"
