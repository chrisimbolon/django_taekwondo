from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Ethiopia's regions and major cities"

    def handle(self, *args, **kwargs):
        country = "ET"  # Ethiopia's country code

        ethiopia_data = {
            "Addis Ababa": ["Addis Ababa"],
            "Oromia": ["Adama", "Jimma", "Ambo"],
            "Tigray": ["Mekelle", "Axum"],
            "Amhara": ["Bahir Dar", "Gondar", "Debre Markos"],
            "Southern Nations, Nationalities, and Peoples": ["Hawassa", "Wolaita Sodo"],
            "Somali": ["Jijiga"],
            "Afar": ["Semera"],
        }

        for province_name, cities in ethiopia_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Ethiopia's regions and cities!"))
