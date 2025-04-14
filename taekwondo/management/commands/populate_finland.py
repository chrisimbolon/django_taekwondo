from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Finland's regions and major cities"

    def handle(self, *args, **kwargs):
        country = "FI"  # Finland's country code

        finland_data = {
            "Uusimaa": ["Helsinki", "Espoo", "Vantaa"],
            "Southwest Finland": ["Turku", "Salo", "Parainen"],
            "Satakunta": ["Pori", "Rauma", "Kankaanpää"],
            "Kanta-Häme": ["Hämeenlinna", "Riihimäki", "Forssa"],
            "Pirkanmaa": ["Tampere", "Nokia", "Ylöjärvi"],
            "Päijänne Tavastia": ["Lahti", "Heinola", "Hollola"],
            "Kymenlaakso": ["Kotka", "Kouvola", "Hamina"],
            "South Karelia": ["Lappeenranta", "Imatra"],
            "Southern Savonia": ["Mikkeli", "Savonlinna", "Pieksämäki"],
            "Northern Savonia": ["Kuopio", "Iisalmi", "Varkaus"],
            "North Karelia": ["Joensuu", "Lieksa", "Outokumpu"],
            "Central Finland": ["Jyväskylä", "Saarijärvi", "Jämsä"],
            "South Ostrobothnia": ["Seinäjoki", "Lapua", "Kauhajoki"],
            "Ostrobothnia": ["Vaasa", "Kokkola", "Kristiinankaupunki"],
            "Central Ostrobothnia": ["Kokkola", "Kannus"],
            "North Ostrobothnia": ["Oulu", "Raahe", "Kajaani"],
            "Kainuu": ["Kajaani", "Sotkamo", "Kuhmo"],
            "Lapland": ["Rovaniemi", "Kemi", "Tornio"],
            "Åland": ["Mariehamn"],
        }

        for province_name, cities in finland_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)

            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))

            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)

                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Finland's regions and cities!"))
