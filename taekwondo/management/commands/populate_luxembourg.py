from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Luxembourg's districts and major cities"

    def handle(self, *args, **kwargs):
        country = "LU"  # Luxembourg's country code

        luxembourg_data = {
            "Luxembourg District": ["Luxembourg City", "Esch-sur-Alzette", "Dudelange"],
            "Diekirch District": ["Diekirch", "Ettelbruck", "Wiltz"],
            "Grevenmacher District": ["Grevenmacher", "Remich", "Junglinster"],
        }

        for province_name, cities in luxembourg_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))
        self.stdout.write(self.style.SUCCESS("Database successfully populated with Luxembourg's districts and cities!"))
