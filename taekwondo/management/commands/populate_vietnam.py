from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Vietnam's provinces and major cities"

    def handle(self, *args, **kwargs):
        country = "VN"  # Vietnam's country code

        vietnam_data = {
            "Hanoi": ["Hanoi"],
            "Ho Chi Minh City": ["Ho Chi Minh City", "Thu Duc"],
            "Da Nang": ["Da Nang", "Hoi An", "Tam Ky"],
            "Can Tho": ["Can Tho", "Vinh Long", "Soc Trang"],
            "Hai Phong": ["Hai Phong", "Uong Bi", "Do Son"],
            "Hue": ["Hue", "Dong Ha", "A Luoi"],
            "Nha Trang": ["Nha Trang", "Cam Ranh", "Dien Khanh"],
        }

        for province_name, cities in vietnam_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))
        self.stdout.write(self.style.SUCCESS("Database successfully populated with Vietnam's provinces and cities!"))
