# Overview

## Setup

Use vscode and devcontainers extension

1. `f1` > `Dev Containers: Open folder in container`
2. `cd backend && docker compose up -d` wait until containers are healthy
3. `./load-data.sh && ./run-server.sh`

Services are decoupled from main backend service to have full integration with vscode e.g. test pane is not supported in containerized version.

## Documentation

Head to /docs/ or visit <http://127.0.0.1:7000/> for rest of documentation
