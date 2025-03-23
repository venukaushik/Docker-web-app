# Use the official Python 3.10 slim base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files to the container
COPY app.py .
COPY requirements.txt .

# Install the required Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define the command to run the Flask app
CMD ["python", "app.py"]
