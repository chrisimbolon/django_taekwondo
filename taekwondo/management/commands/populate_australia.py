from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Australia's states and major cities"

    def handle(self, *args, **kwargs):
        country = "AU"  # Australia country code

        australia_data = {
            "New South Wales": ["Sydney", "Newcastle", "Wollongong"],
            "Victoria": ["Melbourne", "Geelong", "Ballarat"],
            "Queensland": ["Brisbane", "Gold Coast", "Cairns"],
            "Western Australia": ["Perth", "Fremantle", "Bunbury"],
            "South Australia": ["Adelaide", "Mount Gambier", "Whyalla"],
            "Tasmania": ["Hobart", "Launceston", "Devonport"],
            "Australian Capital Territory": ["Canberra"],
            "Northern Territory": ["Darwin", "Alice Springs"],
        }

        for province_name, cities in australia_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Australia's states and cities!"))
