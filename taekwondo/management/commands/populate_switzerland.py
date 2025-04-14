from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Switzerland's cantons and major cities"

    def handle(self, *args, **kwargs):
        country = "CH"  # Switzerland's country code

        # Data structure: {"Canton Name": ["City1", "City2", ...]}
        switzerland_data = {
            "Aargau": ["Aarau", "Baden", "Wettingen"],
            "Appenzell Ausserrhoden": ["Herisau", "Teufen", "Heiden"],
            "Appenzell Innerrhoden": ["Appenzell"],
            "Basel-Landschaft": ["Liestal", "Allschwil", "Pratteln"],
            "Basel-Stadt": ["Basel", "Riehen", "Bettingen"],
            "Bern": ["Bern", "Biel/Bienne", "Thun"],
            "Fribourg": ["Fribourg", "Bulle", "Villars-sur-Glâne"],
            "Geneva": ["Geneva", "Carouge", "Lancy"],
            "Glarus": ["Glarus", "Näfels", "Netstal"],
            "Graubünden": ["Chur", "Davos", "Ilanz"],
            "Jura": ["Delémont", "Porrentruy", "Saignelégier"],
            "Luzern": ["Lucerne", "Emmen", "Kriens"],
            "Neuchâtel": ["Neuchâtel", "La Chaux-de-Fonds", "Le Locle"],
            "Nidwalden": ["Stans", "Hergiswil"],
            "Obwalden": ["Sarnen", "Alpnach"],
            "Schaffhausen": ["Schaffhausen", "Neuhausen am Rheinfall", "Stein am Rhein"],
            "Schwyz": ["Schwyz", "Einsiedeln", "Brunnen"],
            "Solothurn": ["Solothurn", "Olten", "Grenchen"],
            "St. Gallen": ["St. Gallen", "Rapperswil-Jona", "Wil"],
            "Ticino": ["Lugano", "Bellinzona", "Locarno"],
            "Thurgau": ["Frauenfeld", "Kreuzlingen", "Arbon"],
            "Uri": ["Altdorf"],
            "Valais": ["Sion", "Brig", "Martigny"],
            "Vaud": ["Lausanne", "Yverdon-les-Bains", "Nyon"],
            "Zug": ["Zug", "Baar"],
            "Zurich": ["Zurich", "Winterthur", "Uster"],
        }

        for canton_name, cities in switzerland_data.items():
            province, created = Province.objects.get_or_create(province_name=canton_name, country=country)

            if created:
                self.stdout.write(self.style.SUCCESS(f"Canton '{canton_name}' added successfully!"))

            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)

                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{canton_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Switzerland's cantons and cities!"))
