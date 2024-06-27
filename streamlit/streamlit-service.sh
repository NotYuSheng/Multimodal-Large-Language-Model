#!/bin/bash

echo "Starting Streamlit app..."
streamlit run /app/app.py --server.enableCORS false --server.enableXsrfProtection false --browser.gatherUsageStats false
