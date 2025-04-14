from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Argentina's provinces and major cities"

    def handle(self, *args, **kwargs):
        country = "AR"  # Argentina's country code

        argentina_data = {
            "Buenos Aires": ["Buenos Aires", "La Plata", "Mar del Plata"],
            "Córdoba": ["Córdoba", "Villa María"],
            "Santa Fe": ["Rosario", "Santa Fe"],
            "Mendoza": ["Mendoza", "San Rafael"],
            "Tucumán": ["San Miguel de Tucumán"],
            "Salta": ["Salta"],
            "Entre Ríos": ["Paraná"],
            "Chaco": ["Resistencia"],
        }

        for province_name, cities in argentina_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Argentina's provinces and cities!"))
