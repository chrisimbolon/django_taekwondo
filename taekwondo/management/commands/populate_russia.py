from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Russia's federal subjects and major cities"

    def handle(self, *args, **kwargs):
        country = "RU"  # Russia's country code

        russia_data = {
            "Moscow": ["Moscow"],
            "Saint Petersburg": ["Saint Petersburg"],
            "Moscow Oblast": ["Khimki", "Podolsk", "Balashikha"],
            "Krasnodar Krai": ["Krasnodar", "Sochi", "Novorossiysk"],
            "Sverdlovsk Oblast": ["Yekaterinburg", "Nizhny Tagil", "Kamensk-Uralsky"],
            "Novosibirsk Oblast": ["Novosibirsk", "Berdsk", "Iskitim"],
            "Tatarstan": ["Kazan", "Naberezhnye Chelny", "Almetyevsk"],
            "Rostov Oblast": ["Rostov-on-Don", "Taganrog", "Shakhty"],
            "Bashkortostan": ["Ufa", "Sterlitamak", "Salavat"],
            "Chelyabinsk Oblast": ["Chelyabinsk", "Magnitogorsk", "Zlatoust"],
            "Samara Oblast": ["Samara", "Tolyatti", "Syzran"],
            "Nizhny Novgorod Oblast": ["Nizhny Novgorod", "Dzerzhinsk", "Arzamas"],
            "Primorsky Krai": ["Vladivostok", "Nakhodka", "Ussuriysk"],
            "Krasnoyarsk Krai": ["Krasnoyarsk", "Norilsk", "Achinsk"],
            "Irkutsk Oblast": ["Irkutsk", "Bratsk", "Angarsk"],
        }

        for region, cities in russia_data.items():
            province, created = Province.objects.get_or_create(province_name=region, country=country)

            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{region}' added successfully!"))

            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)

                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{region}'!"))

        self.stdout.write(self.style.SUCCESS("✅ Russia's regions and major cities have been populated!"))
