#!/bin/bash
# Start the Ollama service in the background
ollama serve &

# Wait for a few seconds to ensure Ollama service is up
sleep 5

# Pull the llava model
ollama pull llava

# Start the Streamlit application in the background
streamlit run --server.enableCORS false --server.enableXsrfProtection false app.py &

# Wait for all background processes to complete
wait
