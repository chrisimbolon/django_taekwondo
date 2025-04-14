from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Czech Republic's regions and major cities"

    def handle(self, *args, **kwargs):
        country = "CZ"  # Czech Republic's country code

        czech_data = {
            "Prague": ["Prague"],
            "Central Bohemian": ["Kladno", "Mladá Boleslav", "Kolín"],
            "South Bohemian": ["České Budějovice", "Písek", "Tábor"],
            "Plzeň": ["Plzeň", "Klatovy", "Rokycany"],
            "Karlovy Vary": ["Karlovy Vary", "Sokolov", "Cheb"],
            "Ústí nad Labem": ["Ústí nad Labem", "Teplice", "Litoměřice"],
            "Liberec": ["Liberec", "Jablonec nad Nisou", "Česká Lípa"],
            "Hradec Králové": ["Hradec Králové", "Pardubice", "Náchod"],
            "Pardubice": ["Pardubice", "Chrudim", "Svitavy"],
            "South Moravian": ["Brno", "Znojmo", "Vyškov"],
            "Olomouc": ["Olomouc", "Prostějov", "Šumperk"],
            "Zlín": ["Zlín", "Uherské Hradiště", "Vsetín"],
            "Moravian-Silesian": ["Ostrava", "Opava", "Karviná"],
        }

        for province_name, cities in czech_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))

            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Czech Republic's regions and cities added!"))
