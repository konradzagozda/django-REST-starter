#!/usr/bin/env bash

set -ex

export $(cat .env | xargs)

export DB_HOST=localhost
export REDIS_HOST=localhost
export RABBITMQ_HOST=localhost
