from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate South Africa's provinces and major cities"

    def handle(self, *args, **kwargs):
        country = "ZA"  # South Africa's country code

        sa_data = {
            "Gauteng": ["Johannesburg", "Pretoria"],
            "Western Cape": ["Cape Town", "Stellenbosch"],
            "KwaZulu-Natal": ["Durban", "Pietermaritzburg"],
            "Eastern Cape": ["Port Elizabeth", "East London"],
            "Free State": ["Bloemfontein"],
            "Limpopo": ["Polokwane"],
            "Mpumalanga": ["Nelspruit"],
            "North West": ["Mahikeng"],
            "Northern Cape": ["Kimberley"],
        }

        for province_name, cities in sa_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with South Africa's provinces and cities!"))
