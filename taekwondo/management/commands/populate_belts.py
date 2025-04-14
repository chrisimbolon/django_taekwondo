from django.core.management.base import BaseCommand
from taekwondo.models import Belt

class Command(BaseCommand):
    help = "Populate predefined Taekwondo belts"

    def handle(self, *args, **kwargs):
        belts_data = [
            {"rank_name": "2nd Dan", "rank_level": 1, "is_black_belt": True},
            {"rank_name": "1st Dan", "rank_level": 2, "is_black_belt": True},
            {"rank_name": "Black", "rank_level": 3, "is_black_belt": True},
            {"rank_name": "Red", "rank_level": 4, "is_black_belt": False},
        ]

        for belt in belts_data:
            obj, created = Belt.objects.get_or_create(
                rank_name=belt["rank_name"],
                defaults={
                    "rank_level": belt["rank_level"],
                    "is_black_belt": belt["is_black_belt"],
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added belt: {belt['rank_name']}"))
            else:
                self.stdout.write(self.style.WARNING(f"Belt already exists: {belt['rank_name']}"))

        self.stdout.write(self.style.SUCCESS("✅ Belt data populated!"))
