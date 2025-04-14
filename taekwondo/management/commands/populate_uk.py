from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate United Kingdom's countries and major cities"

    def handle(self, *args, **kwargs):
        country = "GB"  # United Kingdom's ISO 3166 country code

        uk_data = {
            "England": ["London", "Manchester", "Birmingham", "Liverpool", "Leeds"],
            "Scotland": ["Edinburgh", "Glasgow", "Aberdeen", "Dundee"],
            "Wales": ["Cardiff", "Swansea", "Newport"],
            "Northern Ireland": ["Belfast", "Derry", "Lisburn"]
        }

        for province_name, cities in uk_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)

            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))

            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)

                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("✅ United Kingdom's data seeded successfully!"))
