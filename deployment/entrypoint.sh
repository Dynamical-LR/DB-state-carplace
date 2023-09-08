#!/bin/sh
echo "Running HTTP Server..."
uvicorn rest.settings:application --port 8080 --workers 5