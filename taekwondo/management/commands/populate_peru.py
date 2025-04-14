from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Peru's regions and major cities"

    def handle(self, *args, **kwargs):
        country = "PE"  # Peru's country code

        peru_data = {
            "Lima": ["Lima", "Callao"],
            "Arequipa": ["Arequipa"],
            "Cusco": ["Cusco"],
            "La Libertad": ["Trujillo"],
            "Piura": ["Piura"],
            "Lambayeque": ["Chiclayo"],
            "Junín": ["Huancayo"],
            "Puno": ["Puno"],
        }

        for region, cities in peru_data.items():
            province, created = Province.objects.get_or_create(province_name=region, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{region}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{region}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Peru's regions and cities!"))
