from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Uruguay's departments and major cities"

    def handle(self, *args, **kwargs):
        country = "UY"  # Uruguay's country code

        uruguay_data = {
            "Montevideo": ["Montevideo"],
            "Canelones": ["Las Piedras", "Pando", "Ciudad de la Costa"],
            "Maldonado": ["Maldonado", "Punta del Este"],
            "Salto": ["Salto"],
            "Paysandú": ["Paysandú"],
            "Colonia": ["Colonia del Sacramento"],
        }

        for department, cities in uruguay_data.items():
            province, created = Province.objects.get_or_create(province_name=department, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{department}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{department}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Uruguay's departments and cities!"))
