#!/usr/bin/env bash

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
else
    echo "-- Models already pulled --"
fi

# Check if the model was pulled successfully
if [ $? -eq 0 ]; then
    echo "Successfully pulled llava model."
else
    echo "Failed to pull llava model."
    exit 1
fi
