from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate India's states and major cities"

    def handle(self, *args, **kwargs):
        country = "IN"  # India's country code

        india_data = {
            "Maharashtra": ["Mumbai", "Pune", "Nagpur"],
            "Delhi": ["New Delhi", "Dwarka", "Rohini"],
            "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai"],
            "Karnataka": ["Bangalore", "Mysore", "Mangalore"],
            "West Bengal": ["Kolkata", "Howrah", "Durgapur"],
            "Uttar Pradesh": ["Lucknow", "Kanpur", "Varanasi"],
            "Gujarat": ["Ahmedabad", "Surat", "Vadodara"],
        }

        for state, cities in india_data.items():
            province, created = Province.objects.get_or_create(province_name=state, country=country)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{state}' added successfully!"))
            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)
                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{state}'!"))
        self.stdout.write(self.style.SUCCESS("Database successfully populated with India's states and cities!"))
