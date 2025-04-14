from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Cuba's provinces and major cities"

    def handle(self, *args, **kwargs):
        country = "CU"  # Cuba's country code

        cuba_data = {
            "Havana": ["Havana"],
            "Santiago de Cuba": ["Santiago de Cuba"],
            "Camagüey": ["Camagüey"],
            "Holguín": ["Holguín"],
            "Cienfuegos": ["Cienfuegos"],
            "Santa Clara": ["Santa Clara"],
            "Guantánamo": ["Guantánamo"],
            "Bayamo": ["Bayamo"],
            "Matanzas": ["Matanzas"],
            "Pinar del Río": ["Pinar del Río"],
        }

        for province_name, cities in cuba_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Cuba's provinces and cities!"))
