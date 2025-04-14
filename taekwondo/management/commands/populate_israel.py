from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Israel's districts and major cities"

    def handle(self, *args, **kwargs):
        country = "IL"  # Israel's country code

        israel_data = {
            "Central District": ["Petah Tikva", "Netanya", "Herzliya"],
            "Haifa District": ["Haifa", "Hadera"],
            "Jerusalem District": ["Jerusalem"],
            "Northern District": ["Nazareth", "Tiberias"],
            "Southern District": ["Beersheba", "Eilat"],
            "Tel Aviv District": ["Tel Aviv", "Bat Yam"],
        }

        for province_name, cities in israel_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Israel's districts and cities!"))
