# Overview

## Setup

1. `cd backend && poetry install && cp env/dev.env .env`
2. `docker compose up -d` wait until services are healthy
3. `poetry shell` initialize venv
4. `python manage.py runserver`
5. `./load-data.sh`

Services are decoupled from main backend service to have full integration with vscode e.g. test pane is not supported in containerized version.

## Documentation

Head to /docs/ or visit <http://127.0.0.1:7000/> for rest of documentation
