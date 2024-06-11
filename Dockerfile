# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Update package list
RUN apt-get update

# Install packages
# pciutils: Needed for lspci, automatic GPU detection
RUN apt-get update && apt-get install -y \
    pciutils \
    curl \
    nano \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Update pip
RUN pip install --upgrade pip

# Install the necessary packages
RUN pip install --no-cache-dir -r requirements.txt

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Copy the rest of the application code into the container
COPY . .

# Expose the ports
EXPOSE 8501
EXPOSE 11434

# Make the start script executable
RUN chmod +x /app/start_services.sh

# Command to run the application
CMD ["/bin/bash", "-c", "/app/start_services.sh"]

# Set the Streamlit app as the entry point
ENTRYPOINT ["/bin/bash", "-c", "streamlit run /app/app.py --server.enableCORS false --server.enableXsrfProtection false"]

