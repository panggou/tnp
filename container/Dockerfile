# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python dependencies file and install them
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the Python script and other necessary files into the container
COPY . .

# Expose the port on which your Flask application will run
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
