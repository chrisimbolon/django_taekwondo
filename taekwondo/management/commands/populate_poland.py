from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Poland's voivodeships and major cities"

    def handle(self, *args, **kwargs):
        country = "PL"  # Poland's country code

        poland_data = {
            "Masovian": ["Warsaw", "Radom", "Pruszków"],
            "Silesian": ["Katowice", "Częstochowa", "Gliwice"],
            "Lesser Poland": ["Kraków", "Tarnów", "Nowy Sącz"],
            "Greater Poland": ["Poznań", "Kalisz", "Leszno"],
            "Łódź": ["Łódź", "Piotrków Trybunalski", "Bełchatów"],
            "Subcarpathian": ["Rzeszów", "Przemyśl", "Jarosław"],
            "Lublin": ["Lublin", "Zamość", "Chełm"],
            "Podlaskie": ["Białystok", "Łomża", "Suwalki"],
            "Warmian-Masurian": ["Olsztyn", "Elbląg", "Ełk"],
            "Kuyavian-Pomeranian": ["Bydgoszcz", "Toruń", "Włocławek"],
            "Pomeranian": ["Gdańsk", "Sopot", "Gdynia"],
            "Lubusz": ["Gorzów Wielkopolski", "Zielona Góra", "Świebodzin"],
            "Opole": ["Opole", "Kędzierzyn-Koźle", "Nysa"],
            "West Pomeranian": ["Szczecin", "Koszalin", "Świnoujście"],
        }

        for province_name, cities in poland_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))

            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Poland's voivodeships and cities added!"))
