# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Update package list
RUN apt-get update

# Needed for lspci, automatic GPU detection
RUN apt-get install pciutils

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

# Pull model
RUN ollama pull llava

# Command to run the application
CMD ["bash", "-c", "streamlit run --server.enableCORS false --server.enableXsrfProtection false app.py & ollama serve"]
