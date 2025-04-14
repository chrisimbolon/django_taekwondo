from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Italy's regions and major cities"

    def handle(self, *args, **kwargs):
        country = "IT"  # Italy's country code

        # Data structure: {"Region Name": ["City1", "City2", ...]}
        italy_data = {
            "Abruzzo": ["L'Aquila", "Pescara", "Teramo"],
            "Aosta Valley": ["Aosta"],
            "Apulia": ["Bari", "Lecce", "Taranto"],
            "Basilicata": ["Potenza", "Matera"],
            "Calabria": ["Catanzaro", "Reggio Calabria", "Cosenza"],
            "Campania": ["Naples", "Salerno", "Caserta"],
            "Emilia-Romagna": ["Bologna", "Parma", "Modena"],
            "Friuli Venezia Giulia": ["Trieste", "Udine", "Pordenone"],
            "Lazio": ["Rome", "Latina", "Viterbo"],
            "Liguria": ["Genoa", "La Spezia", "Savona"],
            "Lombardy": ["Milan", "Bergamo", "Brescia"],
            "Marche": ["Ancona", "Pesaro", "Ascoli Piceno"],
            "Molise": ["Campobasso", "Isernia"],
            "Piedmont": ["Turin", "Alessandria", "Novara"],
            "Sardinia": ["Cagliari", "Sassari", "Nuoro"],
            "Sicily": ["Palermo", "Catania", "Messina"],
            "Trentino-Alto Adige": ["Trento", "Bolzano"],
            "Tuscany": ["Florence", "Pisa", "Siena"],
            "Umbria": ["Perugia", "Terni"],
            "Veneto": ["Venice", "Verona", "Padua"],
        }

        for region_name, cities in italy_data.items():
            province, created = Province.objects.get_or_create(province_name=region_name, country=country)

            if created:
                self.stdout.write(self.style.SUCCESS(f"Region '{region_name}' added successfully!"))

            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)

                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{region_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Italy's regions and cities!"))
