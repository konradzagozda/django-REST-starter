#!/usr/bin/env bash

set -ex

python -m pip install poetry

cp backend/env/compose.env backend/.env
