from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Bolivia's departments and major cities"

    def handle(self, *args, **kwargs):
        country = "BO"  # Bolivia's country code

        bolivia_data = {
            "La Paz": ["La Paz", "El Alto"],
            "Cochabamba": ["Cochabamba", "Sacaba"],
            "Santa Cruz": ["Santa Cruz de la Sierra", "Montero"],
            "Oruro": ["Oruro"],
            "Potosí": ["Potosí"],
            "Tarija": ["Tarija"],
            "Chuquisaca": ["Sucre"],
            "Beni": ["Trinidad"],
            "Pando": ["Cobija"],
        }

        for department, cities in bolivia_data.items():
            province, created = Province.objects.get_or_create(province_name=department, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{department}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{department}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Bolivia's departments and cities!"))
