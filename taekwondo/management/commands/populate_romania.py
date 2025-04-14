from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Romania's counties and major cities"

    def handle(self, *args, **kwargs):
        country = "RO"

        romania_data = {
            "Bucharest": ["Bucharest"],
            "Cluj County": ["Cluj-Napoca"],
            "Timiș County": ["Timișoara"],
            "Iași County": ["Iași"],
            "Constanța County": ["Constanța"],
            "Brașov County": ["Brașov"],
            "Dolj County": ["Craiova"],
            "Galați County": ["Galați"],
            "Sibiu County": ["Sibiu"],
            "Bihor County": ["Oradea"],
        }

        for province_name, cities in romania_data.items():
            province, _ = Province.objects.get_or_create(province_name=province_name, country=country)
            for city in cities:
                City.objects.get_or_create(city_name=city, province=province)

        self.stdout.write(self.style.SUCCESS("Romania's counties and cities added!"))
