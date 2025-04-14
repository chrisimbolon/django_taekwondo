from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Kenya's counties and major cities"

    def handle(self, *args, **kwargs):
        country = "KE"  # Kenya's country code

        kenya_data = {
            "Nairobi": ["Nairobi"],
            "Mombasa": ["Mombasa"],
            "Kisumu": ["Kisumu"],
            "Nakuru": ["Nakuru"],
            "Uasin Gishu": ["Eldoret"],
            "Kiambu": ["Thika"],
            "Machakos": ["Machakos"],
            "Nyeri": ["Nyeri"],
            "Meru": ["Meru"],
            "Kakamega": ["Kakamega"],
        }

        for province_name, cities in kenya_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Kenya's counties and cities!"))
