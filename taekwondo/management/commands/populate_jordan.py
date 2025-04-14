from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Jordan's governorates and major cities"

    def handle(self, *args, **kwargs):
        country = "JO"  # Jordan's country code

        jordan_data = {
            "Amman Governorate": ["Amman", "Wadi as-Seer"],
            "Irbid Governorate": ["Irbid", "Ramtha"],
            "Zarqa Governorate": ["Zarqa", "Russeifa"],
            "Balqa Governorate": ["Salt"],
            "Karak Governorate": ["Karak"],
            "Ma'an Governorate": ["Ma'an", "Petra"],
            "Aqaba Governorate": ["Aqaba"],
        }

        for province_name, cities in jordan_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Jordan's governorates and cities!"))
