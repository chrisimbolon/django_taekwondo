from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Belarus's regions and major cities"

    def handle(self, *args, **kwargs):
        country = "BY"  # Belarus's country code

        belarus_data = {
            "Brest Region": ["Brest", "Baranovichi", "Pinsk"],
            "Gomel Region": ["Gomel", "Mozyr", "Zhlobin"],
            "Grodno Region": ["Grodno", "Lida", "Slonim"],
            "Mogilev Region": ["Mogilev", "Bobruisk", "Shklov"],
            "Vitebsk Region": ["Vitebsk", "Orsha", "Polotsk"],
            "Minsk Region": ["Minsk", "Borisov", "Zhodino"],
        }

        for province_name, cities in belarus_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))
        self.stdout.write(self.style.SUCCESS("Database successfully populated with Belarus's regions and cities!"))
