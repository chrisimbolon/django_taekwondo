from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Ireland's provinces and major cities"

    def handle(self, *args, **kwargs):
        country = "IE"  # Ireland's country code

        # Data structure: {"Province Name": ["City1", "City2", ...]}
        ireland_data = {
            "Leinster": ["Dublin", "Kilkenny", "Wexford"],
            "Munster": ["Cork", "Limerick", "Waterford"],
            "Connacht": ["Galway", "Sligo", "Castlebar"],
            "Ulster (Republic of Ireland part)": ["Letterkenny", "Cavan", "Monaghan"],
        }

        for province_name, cities in ireland_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)

            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))

            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)

                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Ireland's provinces and cities!"))
