# usage: ./run-cmd.sh <command>
# 	e.g. ./run-cmd.sh pytest -n 8
# prerequisite: running stack with "docker compose up"


docker compose run -it backend "$*"
