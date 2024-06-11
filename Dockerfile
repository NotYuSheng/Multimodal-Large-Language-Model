# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Update package list
RUN apt-get update

# Needed for lspci, automatic GPU detection
RUN apt-get install -y pciutils

# Install packages
RUN apt-get install -y curl \
    nano

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the necessary packages
RUN pip install --no-cache-dir -r requirements.txt

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Copy the rest of the application code into the container
COPY . .

# Expose the port that Streamlit will run on
EXPOSE 8501

# Make the start script executable
RUN chmod +x /app/start_services.sh

# Command to run the application
CMD ["bash", "-c", "/app/start_services.sh"]
