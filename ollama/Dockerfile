# Use the official Alpine image from the Docker Hub
FROM ollama/ollama

# Install necessary packages
RUN apt-get update && apt-get install -y \
    pciutils \
    curl \
    nano \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the rest of the application code into the container
COPY . .

# Expose any necessary port
EXPOSE 11434

# Make the start script executable
RUN chmod +x /app/ollama-service.sh \
    && ./ollama-service.sh
