# Use the official Ollama image from the Docker Hub
FROM ollama/ollama:0.2.5

# Install necessary packages
RUN apt-get update && apt-get install -y \
    pciutils \
    curl \
    nano \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY ./ollama-build.sh ./ollama-build.sh
COPY ./ollama-startup.sh ./ollama-startup.sh
COPY ./convert_eol.py ./convert_eol.py
COPY ./proxy-server.py ./proxy-server.py

# Expose any necessary port
EXPOSE 11434

# Make the scripts executable
RUN chmod +x /app/ollama-build.sh
RUN chmod +x /app/ollama-startup.sh

# Run the EOL conversion script
RUN python3 /app/convert_eol.py

# Run build sh script
RUN ./ollama-build.sh

# Run script when the container launches
ENTRYPOINT ["/app/ollama-startup.sh"]
