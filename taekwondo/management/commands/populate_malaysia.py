from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Malaysia's states and major cities"

    def handle(self, *args, **kwargs):
        country = "MY"  # Malaysia's country code

        malaysia_data = {
            "Selangor": ["Shah Alam", "Petaling Jaya", "Klang"],
            "Kuala Lumpur": ["Kuala Lumpur"],
            "Penang": ["George Town", "Butterworth", "Bukit Mertajam"],
            "Johor": ["Johor Bahru", "Batu Pahat", "Kluang"],
            "Sabah": ["Kota Kinabalu", "Sandakan", "Tawau"],
            "Sarawak": ["Kuching", "Miri", "Sibu"],
            "Perak": ["Ipoh", "Taiping", "Teluk Intan"],
        }

        for state, cities in malaysia_data.items():
            province, created = Province.objects.get_or_create(province_name=state, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{state}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{state}'!"))
        self.stdout.write(self.style.SUCCESS("Database successfully populated with Malaysia's states and cities!"))
