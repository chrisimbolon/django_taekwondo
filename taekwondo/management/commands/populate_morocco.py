from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Morocco's regions and major cities"

    def handle(self, *args, **kwargs):
        country = "MA"  # Morocco's country code

        morocco_data = {
            "Rabat-Salé-Kénitra": ["Rabat", "Salé", "Kénitra"],
            "Casablanca-Settat": ["Casablanca", "Mohammedia", "El Jadida"],
            "Marrakesh-Safi": ["Marrakesh", "Safi", "Essaouira"],
            "Fès-Meknès": ["Fès", "Meknès"],
            "Tanger-Tetouan-Al Hoceima": ["Tangier", "Tétouan", "Al Hoceima"],
            "Souss-Massa": ["Agadir", "Taroudant"],
            "Beni Mellal-Khenifra": ["Beni Mellal", "Khénifra"],
        }

        for province_name, cities in morocco_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Morocco's regions and cities!"))
