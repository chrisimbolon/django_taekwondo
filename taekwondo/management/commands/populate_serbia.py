from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Serbia's districts and major cities"

    def handle(self, *args, **kwargs):
        country = "RS"

        serbia_data = {
            "Belgrade District": ["Belgrade"],
            "Nišava District": ["Niš"],
            "South Bačka District": ["Novi Sad"],
            "Šumadija District": ["Kragujevac"],
            "Pomoravlje District": ["Jagodina", "Paraćin"],
            "Zlatibor District": ["Užice", "Čajetina"],
            "Toplica District": ["Prokuplje"],
            "Pirot District": ["Pirot"],
            "Jablanica District": ["Leskovac"],
            "Raška District": ["Kraljevo", "Novi Pazar"],
        }

        for province_name, cities in serbia_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))

            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Serbia's districts and cities added!"))
