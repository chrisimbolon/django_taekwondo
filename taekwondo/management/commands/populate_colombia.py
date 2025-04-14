from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Colombia's departments and major cities"

    def handle(self, *args, **kwargs):
        country = "CO"  # Colombia's country code

        colombia_data = {
            "Bogotá": ["Bogotá"],
            "Antioquia": ["Medellín", "Bello", "Envigado"],
            "Valle del Cauca": ["Cali", "Palmira"],
            "Atlántico": ["Barranquilla", "Soledad"],
            "Cundinamarca": ["Soacha", "Zipaquirá"],
            "Santander": ["Bucaramanga"],
            "Bolívar": ["Cartagena"],
            "Risaralda": ["Pereira"],
        }

        for department, cities in colombia_data.items():
            province, created = Province.objects.get_or_create(province_name=department, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{department}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{department}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Colombia's departments and cities!"))
