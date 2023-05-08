#!/usr/bin/env bash -ex
python -m pip install yapf poetry pre-commit isort

cp backend/env/dev.env backend/.env
