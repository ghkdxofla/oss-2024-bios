#!/bin/bash

if [ -f .env ]; then
    export $(cat .env | xargs)
else
    echo ".env file not found. Please create a .env file with the necessary configuration."
    exit 1
fi

echo "Starting Cromwell server on port $PORT..."
java -Dwebservice.port=$PORT -Dwebservice.interface="0.0.0.0" -jar $CROMWELL_JAR server > $LOG_FILE 2>&1 &

sleep 5
CROMWELL_PID=$(ps aux | grep "$CROMWELL_JAR server" | grep -v grep | awk '{print $2}')

if [ -n "$CROMWELL_PID" ]; then
    echo "Cromwell server started successfully with PID $CROMWELL_PID on port $PORT"
    echo "Logs are being written to $LOG_FILE"
else
    echo "Failed to start Cromwell server. Check $LOG_FILE for details."
fi
