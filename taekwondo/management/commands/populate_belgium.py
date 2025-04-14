from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Belgium's regions and major cities"

    def handle(self, *args, **kwargs):
        country = "BE"  # Belgium's country code

        belgium_data = {
            "Flemish Region": ["Antwerp", "Ghent", "Bruges"],
            "Walloon Region": ["Liège", "Namur", "Charleroi"],
            "Brussels-Capital Region": ["Brussels"],
        }

        for region, cities in belgium_data.items():
            province, created = Province.objects.get_or_create(province_name=region, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{region}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{region}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Belgium's regions and cities!"))
