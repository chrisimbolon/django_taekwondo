from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Denmark's regions and major cities"

    def handle(self, *args, **kwargs):
        country = "DK"  # Denmark's country code

        denmark_data = {
            "Capital Region of Denmark": ["Copenhagen", "Frederiksberg", "Hillerød"],
            "Central Denmark Region": ["Aarhus", "Randers", "Silkeborg"],
            "North Denmark Region": ["Aalborg", "Hjørring", "Frederikshavn"],
            "Region of Southern Denmark": ["Odense", "Esbjerg", "Kolding"],
            "Region Zealand": ["Roskilde", "Næstved", "Køge"],
        }

        for region, cities in denmark_data.items():
            province, created = Province.objects.get_or_create(province_name=region, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{region}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{region}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Denmark's regions and cities!"))
