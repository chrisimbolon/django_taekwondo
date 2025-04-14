from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Portugal's districts and major cities"

    def handle(self, *args, **kwargs):
        country = "PT"  # Portugal's country code

        portugal_data = {
            "Lisbon": ["Lisbon", "Sintra", "Amadora"],
            "Porto": ["Porto", "Vila Nova de Gaia", "Matosinhos"],
            "Braga": ["Braga", "Guimarães", "Barcelos"],
            "Coimbra": ["Coimbra", "Figueira da Foz", "Cantanhede"],
            "Aveiro": ["Aveiro", "Ílhavo", "Ovar"],
            "Faro": ["Faro", "Portimão", "Loulé"],
        }

        for province_name, cities in portugal_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))
        self.stdout.write(self.style.SUCCESS("Database successfully populated with Portugal's districts and cities!"))
