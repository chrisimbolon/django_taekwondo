from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populates the database with South Korea's provinces and major cities."

    def handle(self, *args, **kwargs):
        # Country data
        country_name = "South Korea"

        # Province and City data
        provinces_cities = {
            "Gyeonggi-do": ["Suwon", "Seongnam", "Goyang", "Yongin", "Ansan"],
            "Gangwon-do": ["Chuncheon", "Gangneung", "Wonju"],
            "Chungcheongbuk-do": ["Cheongju", "Chungju"],
            "Chungcheongnam-do": ["Asan", "Cheonan"],
            "Jeollabuk-do": ["Jeonju", "Iksan"],
            "Jeollanam-do": ["Mokpo", "Suncheon"],
            "Gyeongsangbuk-do": ["Pohang", "Gumi", "Andong"],
            "Gyeongsangnam-do": ["Changwon", "Jinju"],
            "Jeju-do": ["Jeju City"],  # Special Self-Governing Province
            "Seoul": ["Jongno-gu", "Gangnam-gu", "Songpa-gu"],  # Special City
            "Busan": ["Haeundae-gu", "Seo-gu"],  # Metropolitan City
            "Incheon": ["Namdong-gu", "Bupyeong-gu"],  # Metropolitan City
            "Daegu": ["Jung-gu", "Suseong-gu"],  # Metropolitan City
            "Gwangju": ["Dong-gu", "Buk-gu"],  # Metropolitan City
            "Daejeon": ["Seo-gu", "Yuseong-gu"],  # Metropolitan City
            "Ulsan": ["Nam-gu", "Dong-gu"],  # Metropolitan City
            "Sejong": ["Sejong City"],  # Special Self-Governing City
        }

        # Add provinces and cities
        for province_name, cities in provinces_cities.items():
            province, created = Province.objects.get_or_create(
                province_name=province_name, country=country_name
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))
            
            for city_name in cities:
                city, created = City.objects.get_or_create(city_name=city_name, province=province)
                if created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city_name}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with South Korea's provinces and cities!"))
