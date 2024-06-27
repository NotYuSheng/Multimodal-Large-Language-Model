# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Install packages
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

# Copy the rest of the application code into the container
COPY . .

# Expose the port
EXPOSE 8501

# Make the script is executable
RUN chmod +x /app/streamlit-service.sh 

# Command to run the application
ENTRYPOINT ["/app/streamlit-service.sh"]
