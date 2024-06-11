#!/bin/bash
streamlit run --server.enableCORS false --server.enableXsrfProtection false app.py &
ollama serve &
wait
