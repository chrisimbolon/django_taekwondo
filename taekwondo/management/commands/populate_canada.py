from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Canada's provinces and major cities"

    def handle(self, *args, **kwargs):
        country = "CA"  # Canada country code

        canada_data = {
            "Alberta": ["Calgary", "Edmonton", "Red Deer"],
            "British Columbia": ["Vancouver", "Victoria", "Kelowna"],
            "Manitoba": ["Winnipeg", "Brandon", "Steinbach"],
            "New Brunswick": ["Moncton", "Fredericton", "Saint John"],
            "Newfoundland and Labrador": ["St. John's", "Corner Brook", "Gander"],
            "Nova Scotia": ["Halifax", "Sydney", "Truro"],
            "Ontario": ["Toronto", "Ottawa", "Hamilton"],
            "Prince Edward Island": ["Charlottetown", "Summerside"],
            "Quebec": ["Montreal", "Quebec City", "Laval"],
            "Saskatchewan": ["Saskatoon", "Regina", "Prince Albert"],
            "Northwest Territories": ["Yellowknife", "Hay River"],
            "Nunavut": ["Iqaluit"],
            "Yukon": ["Whitehorse", "Dawson City"],
        }

        for province_name, cities in canada_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Canada's provinces and cities!"))
