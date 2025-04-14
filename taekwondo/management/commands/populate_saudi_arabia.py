from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Saudi Arabia's provinces and major cities"

    def handle(self, *args, **kwargs):
        country = "SA"  # Saudi Arabia's country code

        saudi_data = {
            "Riyadh Province": ["Riyadh", "Al Kharj"],
            "Makkah Province": ["Jeddah", "Mecca", "Taif"],
            "Eastern Province": ["Dammam", "Al Khobar", "Dhahran"],
            "Medina Province": ["Medina", "Yanbu"],
            "Asir Province": ["Abha", "Khamis Mushait"],
            "Qassim Province": ["Buraidah", "Unaizah"],
            "Tabuk Province": ["Tabuk"],
            "Najran Province": ["Najran"],
            "Jazan Province": ["Jazan"],
        }

        for province_name, cities in saudi_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Saudi Arabia's provinces and cities!"))
