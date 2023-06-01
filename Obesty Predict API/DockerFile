# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Set the environment variables
ENV PORT=8080

# Expose the container port
EXPOSE ${PORT}

# Define the command to run the Flask API
CMD ["python", "main.py"]
