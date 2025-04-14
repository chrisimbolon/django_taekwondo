from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Bosnia and Herzegovina's entities and major cities"

    def handle(self, *args, **kwargs):
        country = "BA"

        bosnia_data = {
            "Federation of Bosnia and Herzegovina": ["Sarajevo", "Mostar", "Tuzla"],
            "Republika Srpska": ["Banja Luka", "Prijedor", "Bijeljina"],
            "Brčko District": ["Brčko"],
        }

        for province_name, cities in bosnia_data.items():
            province, _ = Province.objects.get_or_create(province_name=province_name, country=country)
            for city in cities:
                City.objects.get_or_create(city_name=city, province=province)

        self.stdout.write(self.style.SUCCESS("Bosnia and Herzegovina's regions and cities added!"))
