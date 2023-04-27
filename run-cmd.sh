# usage: ./run-cmd.sh pytest
# prerequisite: running stack with "docker compose up"

docker compose run -it backend "$*"
