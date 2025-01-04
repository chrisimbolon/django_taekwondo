from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate database with Iran's provinces and cities"

    def handle(self, *args, **kwargs):
        country = "IR"  # Iran's ISO 3166-1 alpha-2 code
        data = {
            "Tehran": ["Tehran", "Ray", "Shemiranat"],
            "Isfahan": ["Isfahan", "Kashan", "Najafabad"],
            "Shiraz": ["Shiraz", "Marvdasht", "Fasa"],
            "Tabriz": ["Tabriz", "Maragheh", "Ahar"],
            "Mashhad": ["Mashhad", "Neyshabur", "Sabzevar"],
            # Add more provinces and cities as needed
        }

        for province_name, cities in data.items():
            province, created = Province.objects.get_or_create(
                province_name=province_name,
                country=country,
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))

            for city_name in cities:
                city, city_created = City.objects.get_or_create(
                    city_name=city_name,
                    province=province,
                )
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city_name}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Iran's provinces and cities!"))
