#!/bin/bash
if [ "$env" = "dev" ]; then
    uvicorn main.asgi:application --host 0.0.0.0 --port 8000 --reload
else
    gunicorn main.asgi:application --bind 0.0.0.0 --port 8000
fi
