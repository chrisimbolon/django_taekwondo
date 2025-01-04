from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Spain's provinces and cities into the database."

    def handle(self, *args, **options):
        data = {
            "Andalusia": ["Seville", "Malaga", "Cordoba", "Granada", "Cadiz", "Jaen", "Almeria", "Huelva"],
            "Aragon": ["Zaragoza", "Huesca", "Teruel"],
            "Asturias": ["Oviedo"],
            "Balearic Islands": ["Palma"],
            "Canary Islands": ["Las Palmas", "Santa Cruz de Tenerife"],
            "Cantabria": ["Santander"],
            "Castile-La Mancha": ["Toledo", "Ciudad Real", "Albacete", "Cuenca", "Guadalajara"],
            "Castile and Leon": ["Valladolid", "Leon", "Burgos", "Salamanca", "Zamora", "Palencia", "Avila", "Segovia", "Soria"],
            "Catalonia": ["Barcelona", "Tarragona", "Lleida", "Girona"],
            "Extremadura": ["Badajoz", "Caceres"],
            "Galicia": ["A Coruña", "Lugo", "Ourense", "Pontevedra"],
            "Madrid": ["Madrid"],
            "Murcia": ["Murcia"],
            "Navarre": ["Pamplona"],
            "La Rioja": ["Logroño"],
            "Basque Country": ["Bilbao", "San Sebastian", "Vitoria-Gasteiz"],
            "Valencia": ["Valencia", "Alicante", "Castellon"],
            "Ceuta": ["Ceuta"],
            "Melilla": ["Melilla"],
        }

        for province_name, cities in data.items():
            # Create or get the province
            province, created = Province.objects.get_or_create(
                province_name=province_name, country="ES"
            )
            if created:
                self.stdout.write(f"Province '{province_name}' added successfully!")

            # Add cities for the province
            for city_name in cities:
                city, city_created = City.objects.get_or_create(
                    city_name=city_name, province=province
                )
                if city_created:
                    self.stdout.write(f"City '{city_name}' added under '{province_name}'!")

        self.stdout.write("Database successfully populated with Spain's provinces and cities!")
