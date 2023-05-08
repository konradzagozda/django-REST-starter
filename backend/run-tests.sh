#!/usr/bin/env bash -ex

source ./load-env.sh

poetry run pytest
