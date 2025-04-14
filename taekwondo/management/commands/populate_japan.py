from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Japan's prefectures and major cities"

    def handle(self, *args, **kwargs):
        country = "JP"  # Japan's country code

        japan_data = {
            "Tokyo": ["Tokyo", "Hachioji", "Machida"],
            "Osaka": ["Osaka", "Sakai", "Higashiōsaka"],
            "Kanagawa": ["Yokohama", "Kawasaki", "Sagamihara"],
            "Aichi": ["Nagoya", "Toyota", "Okazaki"],
            "Hokkaido": ["Sapporo", "Hakodate", "Asahikawa"],
            "Fukuoka": ["Fukuoka", "Kitakyushu", "Kurume"],
            "Kyoto": ["Kyoto", "Uji", "Maizuru"],
        }

        for prefecture, cities in japan_data.items():
            province, created = Province.objects.get_or_create(province_name=prefecture, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{prefecture}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{prefecture}'!"))
        self.stdout.write(self.style.SUCCESS("Database successfully populated with Japan's prefectures and cities!"))
