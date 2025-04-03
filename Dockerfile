# Use official Python image as base
FROM python:3.11-slim-bullseye

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    build-essential \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Start the Django server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "coachathlete.wsgi:application"]

