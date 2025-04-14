from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Thailand's provinces and major cities"

    def handle(self, *args, **kwargs):
        country = "TH"  # Thailand's country code

        thailand_data = {
            "Bangkok": ["Bangkok"],
            "Chiang Mai": ["Chiang Mai", "Lamphun", "Mae Rim"],
            "Phuket": ["Phuket", "Patong", "Kathu"],
            "Chonburi": ["Pattaya", "Chonburi", "Sriracha"],
            "Nakhon Ratchasima": ["Nakhon Ratchasima", "Pak Chong", "Phimai"],
            "Khon Kaen": ["Khon Kaen", "Chum Phae", "Ban Phai"],
            "Songkhla": ["Hat Yai", "Songkhla", "Sadao"],
        }

        for province_name, cities in thailand_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))
        self.stdout.write(self.style.SUCCESS("Database successfully populated with Thailand's provinces and cities!"))
