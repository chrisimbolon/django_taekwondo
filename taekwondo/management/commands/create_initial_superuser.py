from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = "Creates a superuser from environment variables"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = os.getenv("DJANGO_SU_NAME")
        email = os.getenv("DJANGO_SU_EMAIL")
        password = os.getenv("DJANGO_SU_PASSWORD")

        if not username or not email or not password:
            self.stderr.write("❌ Missing superuser env vars. Skipping.")
            return

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(f"✅ Superuser '{username}' created successfully!")
        else:
            self.stdout.write(f"⚠️ Superuser '{username}' already exists. Skipping.")
