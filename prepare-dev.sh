#/bin/bash -ex
python -m pip install yapf poetry pre-commit

cp backend/env/dev.env backend/.env
