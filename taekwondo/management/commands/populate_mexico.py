from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Mexico's states and major cities"

    def handle(self, *args, **kwargs):
        country = "MX"  # Mexico's country code

        mexico_data = {
            "Aguascalientes": ["Aguascalientes"],
            "Baja California": ["Tijuana", "Mexicali", "Ensenada"],
            "Baja California Sur": ["La Paz", "Los Cabos"],
            "Campeche": ["Campeche", "Ciudad del Carmen"],
            "Chiapas": ["Tuxtla Gutiérrez", "San Cristóbal de las Casas"],
            "Chihuahua": ["Chihuahua", "Ciudad Juárez"],
            "Coahuila": ["Saltillo", "Torreón"],
            "Colima": ["Colima", "Manzanillo"],
            "Durango": ["Durango", "Gómez Palacio"],
            "Guanajuato": ["León", "Guanajuato", "Irapuato"],
            "Guerrero": ["Acapulco", "Chilpancingo"],
            "Hidalgo": ["Pachuca", "Tula de Allende"],
            "Jalisco": ["Guadalajara", "Puerto Vallarta", "Zapopan"],
            "Mexico City": ["Mexico City"],
            "México State": ["Toluca", "Ecatepec"],
            "Michoacán": ["Morelia", "Uruapan"],
            "Morelos": ["Cuernavaca", "Jiutepec"],
            "Nayarit": ["Tepic", "Bahía de Banderas"],
            "Nuevo León": ["Monterrey", "San Nicolás de los Garza"],
            "Oaxaca": ["Oaxaca City", "Salina Cruz"],
            "Puebla": ["Puebla", "Tehuacán"],
            "Querétaro": ["Querétaro"],
            "Quintana Roo": ["Cancún", "Playa del Carmen", "Chetumal"],
            "San Luis Potosí": ["San Luis Potosí", "Soledad de Graciano Sánchez"],
            "Sinaloa": ["Culiacán", "Mazatlán", "Los Mochis"],
            "Sonora": ["Hermosillo", "Ciudad Obregón"],
            "Tabasco": ["Villahermosa"],
            "Tamaulipas": ["Reynosa", "Tampico", "Ciudad Victoria"],
            "Tlaxcala": ["Tlaxcala City"],
            "Veracruz": ["Veracruz", "Xalapa", "Coatzacoalcos"],
            "Yucatán": ["Mérida", "Valladolid"],
            "Zacatecas": ["Zacatecas", "Fresnillo"],
        }

        for state, cities in mexico_data.items():
            province, created = Province.objects.get_or_create(province_name=state, country=country)

            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{state}' added successfully!"))

            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)

                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{state}'!"))

        self.stdout.write(self.style.SUCCESS("✅ Mexico's states and cities populated successfully!"))
