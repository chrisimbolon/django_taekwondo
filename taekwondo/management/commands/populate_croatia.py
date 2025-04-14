from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Croatia's counties and major cities"

    def handle(self, *args, **kwargs):
        country = "HR"

        croatia_data = {
            "City of Zagreb": ["Zagreb"],
            "Split-Dalmatia County": ["Split", "Makarska"],
            "Primorje-Gorski Kotar County": ["Rijeka", "Crikvenica"],
            "Istria County": ["Pula", "Rovinj"],
            "Zadar County": ["Zadar", "Biograd na Moru"],
            "Šibenik-Knin County": ["Šibenik"],
            "Dubrovnik-Neretva County": ["Dubrovnik", "Metković"],
            "Osijek-Baranja County": ["Osijek", "Đakovo"],
            "Vukovar-Srijem County": ["Vukovar", "Vinkovci"],
            "Međimurje County": ["Čakovec"],
        }

        for province_name, cities in croatia_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))

            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Croatia's counties and cities added!"))
