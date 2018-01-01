#!/usr/bin/env bash
GUNICORN_CMD_ARGS="--bind=0.0.0.0:8080" gunicorn hello:app
