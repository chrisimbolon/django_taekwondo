from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate Taiwan's administrative divisions (province-level municipalities and districts) into the database."

    def handle(self, *args, **kwargs):
        taiwan_provinces_and_cities = {
            "Taipei": ["Beitou", "Shilin", "Zhongzheng", "Daan", "Wanhua", "Xinyi", "Songshan", "Nangang", "Wenshan", "Datong", "Zhongshan"],
            "New Taipei": ["Banqiao", "Xinzhuang", "Sanchong", "Tucheng", "Yonghe", "Zhonghe", "Xindian", "Shulin", "Tamsui", "Ruifang"],
            "Taichung": ["Central District", "West District", "North District", "South District", "Beitun", "Xitun", "Nantun", "Fengyuan", "Houli"],
            "Tainan": ["Anping", "West Central", "East District", "South District", "North District", "Yongkang", "Guanmiao", "Xinhua", "Rende"],
            "Kaohsiung": ["Gushan", "Sanmin", "Lingya", "Qianzhen", "Zuoying", "Fengshan", "Nanzi", "Qiaotou", "Luzhu"],
            "Taoyuan": ["Taoyuan District", "Zhongli", "Pingzhen", "Dayuan", "Guishan", "Bade", "Daxi", "Yangmei"],
            "Hsinchu": ["East District", "North District", "Xiangshan"],
            "Keelung": ["Ren'ai", "Zhongzheng", "Xinyi", "Anle", "Nuannuan", "Qidu"],
            "Chiayi": ["West District", "East District"],
            "Hualien": ["Hualien City", "Ji'an", "Shoufeng", "Xincheng"],
            "Taitung": ["Taitung City", "Beinan", "Luye", "Chenggong"],
            "Miaoli": ["Miaoli City", "Toufen", "Zhuolan", "Zhunan"],
            "Changhua": ["Changhua City", "Lukang", "Erlin", "Hemei"],
            "Nantou": ["Nantou City", "Puli", "Zhushan", "Lugu"],
            "Yunlin": ["Douliu", "Huwei", "Beigang", "Dapi"],
            "Pingtung": ["Pingtung City", "Donggang", "Chaozhou", "Hengchun"]
        }

        country = "TW"  # ISO alpha-2 code for Taiwan

        for province_name, cities in taiwan_provinces_and_cities.items():
            province, created = Province.objects.get_or_create(
                province_name=province_name, country=country
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Province '{province_name}' added successfully!"))

            for city_name in cities:
                city, city_created = City.objects.get_or_create(
                    city_name=city_name, province=province
                )
                if city_created:
                    self.stdout.write(
                        self.style.SUCCESS(f"City '{city_name}' added under '{province_name}'!")
                    )

        self.stdout.write(self.style.SUCCESS("Database successfully populated with Taiwan's provinces and cities!"))
