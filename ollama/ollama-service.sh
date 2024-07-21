#!/bin/bash

# Start the Ollama service in the background
echo "Starting Ollama service..."
ollama serve &

# Wait for a few seconds to ensure Ollama service is up
echo "Waiting for Ollama service to start..."
sleep 5

CONTAINER_ALREADY_STARTED="CONTAINER_ALREADY_STARTED_PLACEHOLDER"
if [ ! -e $CONTAINER_ALREADY_STARTED ]; then
    touch $CONTAINER_ALREADY_STARTED
    # Add new models here!
    # Pull the llava model
    echo "Pulling llava model..."
    ollama pull llava

    # Check if the model(s) were pulled successfully
    if [ $? -eq 0 ]; then
        echo "Successfully pulled all model(s)."
    else
        echo "Failed to pull one or more model(s)."
        exit 1
    fi
else
    echo "-- Model(s) already pulled --"
fi

# Run the proxy server
echo "Starting the proxy server..."
python3 proxy-server.py
