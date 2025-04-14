from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Albania's counties and major cities"

    def handle(self, *args, **kwargs):
        country = "AL"  # Albania's country code

        albania_data = {
            "Tirana County": ["Tirana", "Kamëz"],
            "Durrës County": ["Durrës", "Shijak"],
            "Shkodër County": ["Shkodër", "Lezhë"],
            "Elbasan County": ["Elbasan", "Librazhd"],
            "Fier County": ["Fier", "Lushnjë"],
            "Korçë County": ["Korçë", "Pogradec"],
            "Berat County": ["Berat", "Kuçovë"],
        }

        for county, cities in albania_data.items():
            province, created = Province.objects.get_or_create(province_name=county, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{county}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{county}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Albania's counties and cities!"))
