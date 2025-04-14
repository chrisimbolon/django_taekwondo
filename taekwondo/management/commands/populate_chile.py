from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Chile's regions and major cities"

    def handle(self, *args, **kwargs):
        country = "CL"  # Chile's country code

        chile_data = {
            "Santiago Metropolitan": ["Santiago", "Puente Alto", "Maipú"],
            "Valparaíso": ["Valparaíso", "Viña del Mar"],
            "Biobío": ["Concepción", "Talcahuano"],
            "Araucanía": ["Temuco"],
            "Coquimbo": ["La Serena", "Coquimbo"],
            "Los Lagos": ["Puerto Montt", "Osorno"],
            "Maule": ["Talca"],
        }

        for region, cities in chile_data.items():
            province, created = Province.objects.get_or_create(province_name=region, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{region}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{region}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Chile's regions and cities!"))
