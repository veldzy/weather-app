# Use the official Python image as a base image
FROM python:3.12.2-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install Flask and other dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 4000 to the outside world
EXPOSE 4000

# Command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=4000"]