[![build and test](https://github.com/konradzagozda/django-REST-starter/actions/workflows/test.yml/badge.svg)](https://github.com/konradzagozda/django-REST-starter/actions)

## Overview

Template for starting Django Rest Framework projects

## Tools

Click to preview the project in cloudspaces 👇
[![VS Code Container](https://img.shields.io/static/v1?label=VS+Code&message=Container&logo=visualstudiocode&color=007ACC&logoColor=007ACC&labelColor=2C2C32)](https://open.vscode.dev/konradzagozda/django-REST-starter)

### Formatters
- yapf
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)


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
