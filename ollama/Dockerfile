# Use the official Ollama image from the Docker Hub
FROM ollama/ollama:0.2.5

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and application code into the container
COPY requirements.txt .
COPY ./ollama-build.sh ./ollama-build.sh
COPY ./ollama-startup.sh ./ollama-startup.sh
COPY ./convert_eol.py ./convert_eol.py
COPY ./proxy-server.py ./proxy-server.py

# Install necessary packages and Python dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && pip3 install --no-cache-dir -r requirements.txt \
    && apt-get remove -y --purge \
    && rm -rf /var/lib/apt/lists/*

# Make the scripts executable
RUN chmod +x ./ollama-build.sh ./ollama-startup.sh

# Run the EOL conversion script and the build script
RUN python3 ./convert_eol.py && ./ollama-build.sh

# Expose the necessary port
EXPOSE 11434

# Run script when the container launches
ENTRYPOINT ["./ollama-startup.sh"]
