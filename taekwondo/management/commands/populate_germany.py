from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Germany's states and major cities"

    def handle(self, *args, **kwargs):
        country = "DE"  # Germany's country code

        # Data structure: {"State Name": ["City1", "City2", ...]}
        germany_data = {
            "Baden-Württemberg": ["Stuttgart", "Karlsruhe", "Mannheim"],
            "Bavaria": ["Munich", "Nuremberg", "Augsburg"],
            "Berlin": ["Berlin"],
            "Brandenburg": ["Potsdam", "Cottbus", "Brandenburg an der Havel"],
            "Bremen": ["Bremen", "Bremerhaven"],
            "Hamburg": ["Hamburg"],
            "Hesse": ["Frankfurt", "Wiesbaden", "Kassel"],
            "Lower Saxony": ["Hanover", "Braunschweig", "Osnabrück"],
            "Mecklenburg-Western Pomerania": ["Schwerin", "Rostock", "Neubrandenburg"],
            "North Rhine-Westphalia": ["Cologne", "Düsseldorf", "Dortmund"],
            "Rhineland-Palatinate": ["Mainz", "Ludwigshafen", "Koblenz"],
            "Saarland": ["Saarbrücken", "Neunkirchen", "Homburg"],
            "Saxony": ["Dresden", "Leipzig", "Chemnitz"],
            "Saxony-Anhalt": ["Magdeburg", "Halle", "Dessau-Roßlau"],
            "Schleswig-Holstein": ["Kiel", "Lübeck", "Flensburg"],
            "Thuringia": ["Erfurt", "Weimar", "Jena"],
        }

        for state, cities in germany_data.items():
            province, created = Province.objects.get_or_create(province_name=state, country=country)

            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{state}' added successfully!"))

            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)

                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{state}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Germany's states and cities!"))
