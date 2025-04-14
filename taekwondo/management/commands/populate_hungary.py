from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Hungary's counties and major cities"

    def handle(self, *args, **kwargs):
        country = "HU"

        hungary_data = {
            "Budapest": ["Budapest"],
            "Pest County": ["Érd", "Szentendre"],
            "Baranya County": ["Pécs"],
            "Bács-Kiskun County": ["Kecskemét"],
            "Békés County": ["Békéscsaba"],
            "Borsod-Abaúj-Zemplén County": ["Miskolc"],
            "Csongrád-Csanád County": ["Szeged"],
            "Fejér County": ["Székesfehérvár"],
            "Győr-Moson-Sopron County": ["Győr"],
            "Hajdú-Bihar County": ["Debrecen"],
            "Heves County": ["Eger"],
            "Jász-Nagykun-Szolnok County": ["Szolnok"],
            "Komárom-Esztergom County": ["Tatabánya"],
            "Nógrád County": ["Salgótarján"],
            "Somogy County": ["Kaposvár"],
            "Szabolcs-Szatmár-Bereg County": ["Nyíregyháza"],
            "Tolna County": ["Szekszárd"],
            "Vas County": ["Szombathely"],
            "Veszprém County": ["Veszprém"],
            "Zala County": ["Zalaegerszeg"],
        }

        for province_name, cities in hungary_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))

            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Hungary's counties and cities added!"))
