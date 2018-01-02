#!/usr/bin/env bash
#GUNICORN_CMD_ARGS="--bind=0.0.0.0:8080" gunicorn ask.wsgi
# опция бинд передается в ask.wsgi
gunicorn ask.wsgi --bind 0.0.0.0:8000
