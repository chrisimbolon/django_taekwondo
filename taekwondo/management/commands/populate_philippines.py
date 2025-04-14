from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Philippines' provinces and major cities"

    def handle(self, *args, **kwargs):
        country = "PH"  # Philippines' country code

        philippines_data = {
            "Metro Manila": ["Manila", "Quezon City", "Makati", "Pasig", "Taguig"],
            "Cebu": ["Cebu City", "Mandaue", "Lapu-Lapu"],
            "Davao del Sur": ["Davao City", "Digos"],
            "Iloilo": ["Iloilo City", "Passi", "Oton"],
            "Pampanga": ["San Fernando", "Angeles", "Mabalacat"],
            "Batangas": ["Batangas City", "Lipa", "Tanauan"],
            "Benguet": ["Baguio", "La Trinidad", "Itogon"],
        }

        for province_name, cities in philippines_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))
        self.stdout.write(self.style.SUCCESS("Database successfully populated with Philippines' provinces and cities!"))
