from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Netherlands' provinces and major cities"

    def handle(self, *args, **kwargs):
        country = "NL"  # Netherlands' country code

        # Data structure: {"Province Name": ["City1", "City2", ...]}
        netherlands_data = {
            "Drenthe": ["Assen", "Emmen", "Hoogeveen"],
            "Flevoland": ["Lelystad", "Almere", "Dronten"],
            "Friesland": ["Leeuwarden", "Sneek", "Drachten"],
            "Gelderland": ["Arnhem", "Nijmegen", "Apeldoorn"],
            "Groningen": ["Groningen", "Delfzijl", "Veendam"],
            "Limburg": ["Maastricht", "Venlo", "Heerlen"],
            "North Brabant": ["Eindhoven", "Tilburg", "Breda"],
            "North Holland": ["Amsterdam", "Haarlem", "Hilversum"],
            "Overijssel": ["Zwolle", "Enschede", "Deventer"],
            "South Holland": ["Rotterdam", "The Hague", "Leiden"],
            "Utrecht": ["Utrecht", "Amersfoort", "Nieuwegein"],
            "Zeeland": ["Middelburg", "Vlissingen", "Goes"],
        }

        for province_name, cities in netherlands_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)

            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))

            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)

                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Netherlands' provinces and cities!"))
