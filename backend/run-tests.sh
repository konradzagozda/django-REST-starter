#!/usr/bin/env bash

set -ex

source ./load-env.sh

poetry run pytest
