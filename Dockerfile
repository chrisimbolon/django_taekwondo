
FROM python:3.11-slim-bullseye


WORKDIR /app

# Installing system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    build-essential \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 8000

# Starting the Django server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "coachathlete.wsgi:application"]

