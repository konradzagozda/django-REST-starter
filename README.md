## Overview

[![build and test](https://github.com/konradzagozda/django-REST-starter/actions/workflows/test/badge.svg)]

## Tools

[![VS Code Container](https://img.shields.io/static/v1?label=VS+Code&message=Container&logo=visualstudiocode&color=007ACC&logoColor=007ACC&labelColor=2C2C32)](https://open.vscode.dev/konradzagozda/django-REST-starter)

### Formatters
[![yapf](https://github.com/google/yapf/actions/workflows/ci.yml/badge.svg)](https://open.vscode.dev/konradzagozda/django-REST-starter)


### Linters

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

## Setup

Prerequisites:
- vscode
- docker
- dev containers extension


1. `f1` > `Dev Containers: Open folder in container`
2. Your development enviroment is ready!

navigate to `./backend` and try:
- `./run-tests.sh`
- `./run-server.sh`

Services are decoupled from main backend service to have full integration with vscode e.g. test pane is not supported in containerized version.

## Documentation

Head to /docs/ or visit <http://127.0.0.1:7000/> for rest of documentation
