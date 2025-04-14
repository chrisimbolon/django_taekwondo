from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Slovenia's regions and major cities"

    def handle(self, *args, **kwargs):
        country = "SI"

        slovenia_data = {
            "Central Slovenia": ["Ljubljana"],
            "Drava": ["Maribor"],
            "Coastal–Karst": ["Koper"],
            "Upper Carniola": ["Kranj"],
            "Savinja": ["Celje"],
            "Mura": ["Murska Sobota"],
            "Carinthia": ["Slovenj Gradec"],
        }

        for province_name, cities in slovenia_data.items():
            province, _ = Province.objects.get_or_create(province_name=province_name, country=country)
            for city in cities:
                City.objects.get_or_create(city_name=city, province=province)

        self.stdout.write(self.style.SUCCESS("Slovenia's regions and cities added!"))
