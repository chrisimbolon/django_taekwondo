from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Ecuador's provinces and major cities"

    def handle(self, *args, **kwargs):
        country = "EC"  # Ecuador's country code

        ecuador_data = {
            "Pichincha": ["Quito"],
            "Guayas": ["Guayaquil", "Daule"],
            "Azuay": ["Cuenca"],
            "Manabí": ["Portoviejo", "Manta"],
            "Tungurahua": ["Ambato"],
            "El Oro": ["Machala"],
            "Loja": ["Loja"],
            "Imbabura": ["Ibarra"],
        }

        for province_name, cities in ecuador_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Ecuador's provinces and cities!"))
