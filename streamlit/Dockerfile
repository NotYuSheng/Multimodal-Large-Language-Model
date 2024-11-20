# Use the official Python image as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
COPY . .

# Expose the port that Streamlit will run on
EXPOSE 8501

# Run the Streamlit application
CMD ["streamlit", "run", "/app/app.py", "--server.enableCORS", "false", "--server.enableXsrfProtection", "false", "--browser.gatherUsageStats", "false"]

