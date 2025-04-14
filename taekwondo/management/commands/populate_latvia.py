from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Latvia's planning regions and major cities"

    def handle(self, *args, **kwargs):
        country = "LV"  # Latvia's country code

        latvia_data = {
            "Riga Region": ["Riga", "Jūrmala", "Salaspils"],
            "Pierīga Region": ["Ogre", "Sigulda"],
            "Vidzeme Region": ["Valmiera", "Cēsis"],
            "Kurzeme Region": ["Liepāja", "Ventspils", "Kuldīga"],
            "Zemgale Region": ["Jelgava", "Bauska", "Dobele"],
            "Latgale Region": ["Daugavpils", "Rēzekne", "Ludza"],
        }

        for province_name, cities in latvia_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))

            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Latvia's regions and cities added!"))
