from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Slovakia's regions and major cities"

    def handle(self, *args, **kwargs):
        country = "SK"  # Slovakia's country code

        slovakia_data = {
            "Bratislava": ["Bratislava"],
            "Trnava": ["Trnava", "Piešťany", "Hlohovec"],
            "Trenčín": ["Trenčín", "Nové Mesto nad Váhom", "Ilava"],
            "Nitra": ["Nitra", "Levice", "Komárno"],
            "Zvolen": ["Zvolen", "Banská Bystrica", "Žiar nad Hronom"],
            "Košice": ["Košice", "Prešov", "Trebišov"],
            "Prešov": ["Prešov", "Humenné", "Vranov nad Topľou"],
            "Žilina": ["Žilina", "Martin", "Kysucké Nové Mesto"],
        }

        for province_name, cities in slovakia_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))

            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Slovakia's regions and cities added!"))
