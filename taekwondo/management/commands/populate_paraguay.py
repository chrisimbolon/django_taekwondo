from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Paraguay's departments and major cities"

    def handle(self, *args, **kwargs):
        country = "PY"  # Paraguay's country code

        paraguay_data = {
            "Central": ["San Lorenzo", "Luque", "Lambaré"],
            "Capital District": ["Asunción"],
            "Alto Paraná": ["Ciudad del Este"],
            "Itapúa": ["Encarnación"],
            "Caaguazú": ["Coronel Oviedo"],
            "Amambay": ["Pedro Juan Caballero"],
        }

        for department, cities in paraguay_data.items():
            province, created = Province.objects.get_or_create(province_name=department, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{department}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{department}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Paraguay's departments and cities!"))
