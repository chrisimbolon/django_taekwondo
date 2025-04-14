from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Egypt's governorates and major cities"

    def handle(self, *args, **kwargs):
        country = "EG"  # Egypt's country code

        egypt_data = {
            "Cairo": ["Cairo"],
            "Alexandria": ["Alexandria"],
            "Giza": ["Giza", "Sheikh Zayed", "6th of October City"],
            "Dakahlia": ["Mansoura"],
            "Red Sea": ["Hurghada"],
            "Beheira": ["Damanhur"],
            "Aswan": ["Aswan"],
            "Luxor": ["Luxor"],
            "Suez": ["Suez"],
            "Ismailia": ["Ismailia"],
        }

        for province_name, cities in egypt_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Egypt's governorates and cities!"))
