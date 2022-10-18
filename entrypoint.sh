#!/bin/bash
if [ "$env" = "dev" ]; then
    gunicorn main.wsgi -w 2 --bind :8000 --reload
else
    gunicorn main.asgi -w 10 --bind :8000
fi
