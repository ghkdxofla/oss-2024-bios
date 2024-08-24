#!/bin/bash

if [ -f .env ]; then
    export $(cat .env | xargs)
else
    echo ".env file not found. Please create a .env file with the necessary configuration."
    exit 1
fi

echo "Stopping Cromwell server..."

CROMWELL_PID=$(ps aux | grep "$CROMWELL_JAR server" | grep -v grep | awk '{print $2}')

if [ -n "$CROMWELL_PID" ]; then
    kill $CROMWELL_PID
    echo "Cromwell server with PID $CROMWELL_PID has been stopped."
else
    echo "Cromwell server is not running."
fi
