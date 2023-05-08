#!/usr/bin/env bash

set -ex

python -m pip install poetry

cp backend/env/dev.env backend/.env
