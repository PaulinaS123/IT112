HEAD
# Use an official Python runtime as a parent image
FROM python:3.11-slim


FROM python:3.9-slim
67e4acb (Initial commit: add django project files)

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port Django will run on
EXPOSE 8000

HEAD
# Run the Django server
# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port Django will run on
EXPOSE 8000

# Run the Django server
b10d5fe (Initial commit: add django project files)
67e4acb (Initial commit: add django project files)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
