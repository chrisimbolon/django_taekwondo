from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Lithuania's counties and major cities"

    def handle(self, *args, **kwargs):
        country = "LT"  # Lithuania's country code

        lithuania_data = {
            "Vilnius County": ["Vilnius", "Šalčininkai", "Trakai"],
            "Kaunas County": ["Kaunas", "Jonava", "Kėdainiai"],
            "Klaipėda County": ["Klaipėda", "Palanga", "Šilutė"],
            "Šiauliai County": ["Šiauliai", "Joniškis", "Kuršėnai"],
            "Panevėžys County": ["Panevėžys", "Biržai", "Pasvalys"],
            "Alytus County": ["Alytus", "Varėna", "Lazdijai"],
            "Marijampolė County": ["Marijampolė", "Šakiai"],
            "Tauragė County": ["Tauragė", "Pagėgiai"],
            "Telšiai County": ["Telšiai", "Plungė", "Mažeikiai"],
            "Utena County": ["Utena", "Zarasai", "Ignalina"],
        }

        for province_name, cities in lithuania_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))

            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Lithuania's counties and cities added!"))
