from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Bulgaria's provinces and major cities"

    def handle(self, *args, **kwargs):
        country = "BG"

        bulgaria_data = {
            "Sofia Province": ["Sofia"],
            "Plovdiv Province": ["Plovdiv", "Asenovgrad"],
            "Varna Province": ["Varna"],
            "Burgas Province": ["Burgas"],
            "Stara Zagora Province": ["Stara Zagora"],
            "Ruse Province": ["Ruse"],
            "Pleven Province": ["Pleven"],
            "Sliven Province": ["Sliven"],
            "Dobrich Province": ["Dobrich"],
            "Shumen Province": ["Shumen"],
        }

        for province_name, cities in bulgaria_data.items():
            province, _ = Province.objects.get_or_create(province_name=province_name, country=country)
            for city in cities:
                City.objects.get_or_create(city_name=city, province=province)

        self.stdout.write(self.style.SUCCESS("Bulgaria's provinces and cities added!"))
