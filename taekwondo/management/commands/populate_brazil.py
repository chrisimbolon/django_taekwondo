from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Brazil's states and major cities"

    def handle(self, *args, **kwargs):
        country = "BR"  # Brazil's country code

        brazil_data = {
            "São Paulo": ["São Paulo", "Campinas", "Santos"],
            "Rio de Janeiro": ["Rio de Janeiro", "Niterói", "Petrópolis"],
            "Minas Gerais": ["Belo Horizonte", "Uberlândia", "Contagem"],
            "Bahia": ["Salvador", "Feira de Santana", "Vitória da Conquista"],
            "Paraná": ["Curitiba", "Londrina", "Maringá"],
            "Rio Grande do Sul": ["Porto Alegre", "Caxias do Sul", "Pelotas"],
            "Pernambuco": ["Recife", "Olinda", "Jaboatão dos Guararapes"],
            "Ceará": ["Fortaleza", "Caucaia", "Juazeiro do Norte"],
            "Pará": ["Belém", "Ananindeua", "Santarém"],
            "Santa Catarina": ["Florianópolis", "Joinville", "Blumenau"],
            "Goiás": ["Goiânia", "Anápolis", "Aparecida de Goiânia"],
            "Amazonas": ["Manaus", "Parintins", "Itacoatiara"],
            "Maranhão": ["São Luís", "Imperatriz", "Timon"],
            "Espírito Santo": ["Vitória", "Vila Velha", "Serra"],
            "Mato Grosso": ["Cuiabá", "Várzea Grande", "Rondonópolis"],
            "Distrito Federal": ["Brasília"],
        }

        for state, cities in brazil_data.items():
            province, created = Province.objects.get_or_create(province_name=state, country=country)

            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{state}' added successfully!"))

            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)

                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{state}'!"))

        self.stdout.write(self.style.SUCCESS("✅ Brazil's states and major cities have been added!"))
