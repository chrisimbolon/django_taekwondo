from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Ukraine's oblasts and major cities"

    def handle(self, *args, **kwargs):
        country = "UA"  # Ukraine's country code

        ukraine_data = {
            "Vinnytsia Oblast": ["Vinnytsia", "Zhmerynka", "Koziatyn"],
            "Volyn Oblast": ["Lutsk", "Kovel", "Volodymyr"],
            "Dnipropetrovsk Oblast": ["Dnipro", "Kryvyi Rih", "Kamianske"],
            "Donetsk Oblast": ["Donetsk", "Mariupol", "Kramatorsk"],
            "Zhytomyr Oblast": ["Zhytomyr", "Berdychiv", "Korosten"],
            "Zakarpattia Oblast": ["Uzhhorod", "Mukachevo", "Khust"],
            "Zaporizhzhia Oblast": ["Zaporizhzhia", "Melitopol", "Berdyansk"],
            "Ivano-Frankivsk Oblast": ["Ivano-Frankivsk", "Kolomyia", "Kalush"],
            "Kyiv Oblast": ["Bila Tserkva", "Boryspil", "Brovary"],
            "Kirovohrad Oblast": ["Kropyvnytskyi", "Oleksandriia", "Svitlovodsk"],
            "Luhansk Oblast": ["Luhansk", "Sievierodonetsk", "Alchevsk"],
            "Lviv Oblast": ["Lviv", "Drohobych", "Stryi"],
            "Mykolaiv Oblast": ["Mykolaiv", "Voznesensk", "Yuzhnoukrainsk"],
            "Odesa Oblast": ["Odesa", "Izmail", "Bilhorod-Dnistrovskyi"],
            "Poltava Oblast": ["Poltava", "Kremenchuk", "Lubny"],
            "Rivne Oblast": ["Rivne", "Dubno", "Kostopil"],
            "Sumy Oblast": ["Sumy", "Konotop", "Shostka"],
            "Ternopil Oblast": ["Ternopil", "Chortkiv", "Berezhany"],
            "Kharkiv Oblast": ["Kharkiv", "Lozova", "Izium"],
            "Kherson Oblast": ["Kherson", "Nova Kakhovka", "Skadovsk"],
            "Khmelnytskyi Oblast": ["Khmelnytskyi", "Kamianets-Podilskyi", "Shepetivka"],
            "Cherkasy Oblast": ["Cherkasy", "Uman", "Zolotonosha"],
            "Chernivtsi Oblast": ["Chernivtsi", "Khotyn", "Storozhynets"],
            "Chernihiv Oblast": ["Chernihiv", "Nizhyn", "Pryluky"],
            "Kyiv (City)": ["Kyiv"],
            "Sevastopol": ["Sevastopol"],
            "Crimea (Autonomous Republic)": ["Simferopol", "Yalta", "Kerch"],
        }

        for province_name, cities in ukraine_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)

            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))

            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)

                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Ukraine's oblasts and cities!"))
