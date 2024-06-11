#!/bin/bash

# Start the Ollama service in the background
echo "Starting Ollama service..."
ollama serve &

# Wait for a few seconds to ensure Ollama service is up
echo "Waiting for Ollama service to start..."
sleep 5

# Pull the llava model
echo "Pulling llava model..."
ollama pull llava

# Check if the model was pulled successfully
if [ $? -eq 0 ]; then
    echo "Successfully pulled llava model."
else
    echo "Failed to pull llava model."
    exit 1
fi

# Start the Streamlit application in the background
echo "Starting Streamlit application..."
nohup streamlit run --server.enableCORS false --server.enableXsrfProtection false app.py &

#echo "All services startup completed"
