#!/bin/bash

# Start the Ollama service in the background
echo "Starting Ollama service..."
ollama serve &

# Run the proxy server
echo "Starting the proxy server..."
python3 /app/proxy-server.py
