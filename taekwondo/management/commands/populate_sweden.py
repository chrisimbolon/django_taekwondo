from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Sweden's counties and major cities"

    def handle(self, *args, **kwargs):
        country = "SE"  # Sweden's country code

        sweden_data = {
            "Stockholm County": ["Stockholm", "Södertälje", "Täby"],
            "Uppsala County": ["Uppsala", "Enköping", "Tierp"],
            "Södermanland County": ["Eskilstuna", "Nyköping", "Katrineholm"],
            "Östergötland County": ["Linköping", "Norrköping", "Motala"],
            "Jönköping County": ["Jönköping", "Värnamo", "Nässjö"],
            "Kronoberg County": ["Växjö", "Ljungby", "Älmhult"],
            "Kalmar County": ["Kalmar", "Västervik", "Oskarshamn"],
            "Gotland County": ["Visby"],
            "Blekinge County": ["Karlskrona", "Ronneby", "Karlshamn"],
            "Skåne County": ["Malmö", "Lund", "Helsingborg"],
            "Halland County": ["Halmstad", "Varberg", "Falkenberg"],
            "Västra Götaland County": ["Gothenburg", "Borås", "Trollhättan"],
            "Värmland County": ["Karlstad", "Arvika", "Kristinehamn"],
            "Örebro County": ["Örebro", "Kumla", "Hallsberg"],
            "Västmanland County": ["Västerås", "Köping", "Sala"],
            "Dalarna County": ["Falun", "Borlänge", "Avesta"],
            "Gävleborg County": ["Gävle", "Hudiksvall", "Sandviken"],
            "Västernorrland County": ["Sundsvall", "Härnösand", "Örnsköldsvik"],
            "Jämtland County": ["Östersund", "Strömsund", "Bräcke"],
            "Västerbotten County": ["Umeå", "Skellefteå", "Lycksele"],
            "Norrbotten County": ["Luleå", "Kiruna", "Boden"],
        }

        for province_name, cities in sweden_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)

            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))

            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)

                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Sweden's counties and cities!"))
