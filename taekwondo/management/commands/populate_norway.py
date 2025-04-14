from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Norway's counties and major cities"

    def handle(self, *args, **kwargs):
        country = "NO"  # Norway's country code

        norway_data = {
            "Viken": ["Drammen", "Bærum", "Sarpsborg"],
            "Oslo": ["Oslo"],
            "Innlandet": ["Hamar", "Lillehammer", "Gjøvik"],
            "Vestfold og Telemark": ["Skien", "Tønsberg", "Sandefjord"],
            "Agder": ["Kristiansand", "Arendal", "Grimstad"],
            "Rogaland": ["Stavanger", "Sandnes", "Haugesund"],
            "Vestland": ["Bergen", "Stord", "Førde"],
            "Møre og Romsdal": ["Ålesund", "Molde", "Kristiansund"],
            "Trøndelag": ["Trondheim", "Steinkjer", "Stjørdal"],
            "Nordland": ["Bodø", "Mo i Rana", "Narvik"],
            "Troms og Finnmark": ["Tromsø", "Alta", "Hammerfest"],
        }

        for province_name, cities in norway_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)

            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))

            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)

                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Norway's counties and cities!"))
