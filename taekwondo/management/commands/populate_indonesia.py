from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Indonesia's provinces and major cities"

    def handle(self, *args, **kwargs):
        country = "ID"  # Indonesia's country code

        indonesia_data = {
            "Aceh": ["Banda Aceh", "Lhokseumawe", "Langsa"],
            "North Sumatra": ["Medan", "Binjai", "Pematangsiantar"],
            "West Sumatra": ["Padang", "Bukittinggi", "Payakumbuh"],
            "Riau": ["Pekanbaru", "Dumai", "Siak"],
            "Riau Islands": ["Batam", "Tanjung Pinang", "Karimun"],
            "Jambi": ["Jambi", "Muara Bungo", "Sungai Penuh"],
            "South Sumatra": ["Palembang", "Lubuklinggau", "Prabumulih"],
            "Bangka Belitung Islands": ["Pangkal Pinang", "Tanjung Pandan"],
            "Bengkulu": ["Bengkulu", "Curup", "Manna"],
            "Lampung": ["Bandar Lampung", "Metro", "Kotabumi"],
            "Banten": ["Serang", "Tangerang", "Cilegon"],
            "Jakarta": ["Central Jakarta", "South Jakarta", "East Jakarta", "North Jakarta", "West Jakarta"],
            "West Java": ["Bandung", "Bekasi", "Bogor"],
            "Central Java": ["Semarang", "Surakarta", "Purwokerto"],
            "Yogyakarta": ["Yogyakarta", "Sleman", "Bantul"],
            "East Java": ["Surabaya", "Malang", "Kediri"],
            "Bali": ["Denpasar", "Singaraja", "Tabanan"],
            "West Kalimantan": ["Pontianak", "Singkawang", "Sambas"],
            "Central Kalimantan": ["Palangka Raya", "Pangkalan Bun", "Sampit"],
            "South Kalimantan": ["Banjarmasin", "Banjarbaru", "Martapura"],
            "East Kalimantan": ["Samarinda", "Balikpapan", "Bontang"],
            "North Sulawesi": ["Manado", "Bitung", "Tomohon"],
            "Central Sulawesi": ["Palu", "Poso", "Luwuk"],
            "South Sulawesi": ["Makassar", "Parepare", "Palopo"],
            "Southeast Sulawesi": ["Kendari", "Baubau", "Kolaka"],
            "Gorontalo": ["Gorontalo", "Limboto", "Tilamuta"],
            "West Sulawesi": ["Mamuju", "Polewali", "Majene"],
            "Maluku": ["Ambon", "Masohi", "Tual"],
            "North Maluku": ["Ternate", "Tidore", "Sofifi"],
            "West Papua": ["Manokwari", "Sorong"],
            "Southwest Papua": ["Fakfak", "Kaimana"],
            "Central Papua": ["Nabire", "Timika"],
            "Highland Papua": ["Wamena", "Dekai"],
            "Papua": ["Jayapura", "Sentani", "Merauke"],
        }

        for province_name, cities in indonesia_data.items():
            province, created = Province.objects.get_or_create(province_name=province_name, country=country)

            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))

            for city in cities:
                city_obj, city_created = City.objects.get_or_create(city_name=city, province=province)

                if city_created:
                    self.stdout.write(self.style.SUCCESS(f"City '{city}' added under '{province_name}'!"))

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Indonesia's provinces and cities!"))
