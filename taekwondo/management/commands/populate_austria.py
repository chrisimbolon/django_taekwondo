from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Austria's states and major cities"

    def handle(self, *args, **kwargs):
        country = "AT"  # Austria's country code

        # Data structure: {"State Name": ["City1", "City2", ...]}
        austria_data = {
            "Burgenland": ["Eisenstadt", "Oberwart", "Neusiedl am See"],
            "Carinthia": ["Klagenfurt", "Villach", "Wolfsberg"],
            "Lower Austria": ["St. Pölten", "Wr. Neustadt", "Krems"],
            "Upper Austria": ["Linz", "Wels", "Steyr"],
            "Salzburg": ["Salzburg", "Hallein", "Saalfelden"],
            "Styria": ["Graz", "Leoben", "Kapfenberg"],
            "Tyrol": ["Innsbruck", "Kufstein", "Lienz"],
            "Vorarlberg": ["Bregenz", "Dornbirn", "Feldkirch"],
            "Vienna": ["Vienna"],
        }

        for state_name, cities in austria_data.items():
            province, created = Province.objects.get_or_create(province_name=state_name, country=country)

            if created:
                self.stdout.write(self.style.SUCCESS(f"State '{state_name}' added successfully!"))

            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)

                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{state_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Austria's states and cities!"))
