# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory within the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Specify the command to run your Python script
CMD ["python", "Execution.py"]
