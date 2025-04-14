from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Nigeria's states and major cities"

    def handle(self, *args, **kwargs):
        country = "NG"  # Nigeria's country code

        nigeria_data = {
            "Lagos": ["Lagos", "Ikeja"],
            "Abuja (FCT)": ["Abuja"],
            "Kano": ["Kano", "Wudil"],
            "Rivers": ["Port Harcourt", "Bonny"],
            "Kaduna": ["Kaduna", "Zaria"],
            "Oyo": ["Ibadan", "Ogbomosho"],
            "Anambra": ["Awka", "Onitsha"],
            "Enugu": ["Enugu"],
            "Edo": ["Benin City"],
            "Borno": ["Maiduguri"],
        }

        for province_name, cities in nigeria_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Nigeria's states and cities!"))
