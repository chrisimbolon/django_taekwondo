from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate France's regions and major cities"

    def handle(self, *args, **kwargs):
        country = "FR"  # France's country code

        france_data = {
            "Île-de-France": ["Paris", "Boulogne-Billancourt", "Saint-Denis"],
            "Provence-Alpes-Côte d'Azur": ["Marseille", "Nice", "Toulon"],
            "Auvergne-Rhône-Alpes": ["Lyon", "Grenoble", "Clermont-Ferrand"],
            "Nouvelle-Aquitaine": ["Bordeaux", "Limoges", "Poitiers"],
            "Occitanie": ["Toulouse", "Montpellier", "Nîmes"],
            "Hauts-de-France": ["Lille", "Amiens", "Roubaix"],
            "Grand Est": ["Strasbourg", "Metz", "Reims"],
            "Brittany": ["Rennes", "Brest", "Quimper"],
            "Normandy": ["Caen", "Rouen", "Le Havre"],
            "Pays de la Loire": ["Nantes", "Angers", "Le Mans"],
            "Centre-Val de Loire": ["Orléans", "Tours", "Bourges"],
            "Bourgogne-Franche-Comté": ["Dijon", "Besançon", "Auxerre"],
            "Corsica": ["Ajaccio", "Bastia"],
        }

        for region, cities in france_data.items():
            province, created = Province.objects.get_or_create(province_name=region, country=country)

            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{region}' added successfully!"))

            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)

                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{region}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with France's regions and cities!"))
