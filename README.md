# 🥋 Django Taekwondo Coach

Django Taekwondo Coach is a media-rich web application built to help coaches manage training videos, athlete resources, and performance data. Developed with Django and PostgreSQL, this app features media uploads, admin control, and production-grade deployment using Docker, a flexible CI/CD pipeline using GitHub Actions, NGINX, and Caddy.
It runs under a custom subdomain and supports both local and production environments.

# 🚀 Features

- 🧑🏫 Coach & athlete management
- 📦 Dockerized for local and production deployment
- 🐘 PostgreSQL database
- 🌍 Subdomain-based routing support (e.g. taekwondo-coach.chrisimbolon.dev`)
- ⚙ NGINX (Production only)
- 🔄 CI/CD with GitHub Actions
- 🧪 Environment-based settings with ` .env python-dotenv
- 💾 File/media upload support
- 🧹 Static file collection via `collectstatic`
  `

# 🧱 Tech Stack

- Backend: Django, Gunicorn
- Database: PostgreSQL 15
- Static Media: Cloudinary, Local Volume (media/, static/)
- Web Server: NGINX (for production), Docker networking
- Docker + Docker Compose
- CI/CD: GitHub Actions
- Reverse Proxy: Caddy (subdomain routing + HTTPS)

# 🚀 Live Demo

[https://taekwondo-coach.chrisimbolon.dev/]

# 🛠 Local Development Setup

> This setup skips NGINX for simplicity.

## 1. Clone the repo

```bash
git clone https://github.com/yourusername/djangotaekwondocoach.git
cd djangotaekwondocoach
```

## 2. Create a .env file

### .env

```
POSTGRES_DB=taekwondodb
POSTGRES_USER=taekwondouser
POSTGRES_PASSWORD=securepassword
POSTGRES_PORT=5432
POSTGRES_HOST=db
SECRET_KEY=yourdjangosecret
ALLOWED_HOSTS=localhost,127.0.0.1
```

## 3. Run Docker Compose

```
docker-compose up --build
```

# Production Deployment

Production setup is intended for deployment on a server (e.g., DigitalOcean) behind Caddy as the main
reverse proxy, and NGINX as an internal proxy to serve static files.
Key differences in prod:
nginx service is used.
Caddy handles domain routing and HTTPS.
Django is served by Gunicorn behind NGINX.
Static and media files are served from mounted volumes.
You can customize the deployment with a Caddyfile like:

caddy
taekwondo-coach.chrisimbolon.dev {
reverse
\_proxy djangotaekwondocoach-nginx:80
}

# CI/CD

GitHub Actions is used to:

1. Build the Docker image.
2. SSH into your DigitalOcean droplet.
3. Pull the latest code.
4. Rebuild and restart the app via Docker Compose.
   Sample GitHub Actions workflow file: .github/workflows/deploy.yml

# Project Structure

```
├── Dockerfile
├── docker-compose.yml
├── docker-compose.override.yml
├── coachathlete/
│ └── settings.py
├── taekwondo/
│ └── views.py, models.py, ...
├── templates/
├── static/
├── media/
└── requirements.txt
```

Author
Christyan Simbolon
🔗 chrisimbolon.dev
🐙 github.com/chrisimbolon
