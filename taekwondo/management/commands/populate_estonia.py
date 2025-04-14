from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Estonia's counties and major cities"

    def handle(self, *args, **kwargs):
        country = "EE"  # Estonia's country code

        estonia_data = {
            "Harju County": ["Tallinn", "Maardu", "Keila"],
            "Tartu County": ["Tartu", "Elva", "Kallaste"],
            "Ida-Viru County": ["Narva", "Kohtla-Järve", "Sillamäe"],
            "Pärnu County": ["Pärnu", "Kihnu", "Sindi"],
            "Viljandi County": ["Viljandi", "Karksi-Nuia"],
            "Rapla County": ["Rapla", "Kohila"],
            "Jõgeva County": ["Jõgeva", "Põltsamaa"],
            "Lääne County": ["Haapsalu"],
            "Lääne-Viru County": ["Rakvere", "Tapa"],
            "Valga County": ["Valga", "Tõrva"],
            "Võru County": ["Võru", "Antsla"],
            "Saare County": ["Kuressaare"],
            "Hiiu County": ["Kärdla"],
            "Järva County": ["Paide"],
        }

        for province_name, cities in estonia_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))

            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Estonia's counties and cities added!"))
