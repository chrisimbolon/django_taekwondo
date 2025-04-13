from django.core.management.base import BaseCommand
from taekwondo.models import Province, City

class Command(BaseCommand):
    help = "Populate China's provinces and major cities into the database"

    def handle(self, *args, **kwargs):
        country = "CN"

        data = {
            "Beijing": ["Dongcheng", "Xicheng", "Chaoyang", "Haidian"],
            "Shanghai": ["Huangpu", "Xuhui", "Changning", "Pudong"],
            "Tianjin": ["Heping", "Nankai", "Hexi", "Dongli"],
            "Chongqing": ["Yuzhong", "Jiangbei", "Shapingba", "Nan'an"],
            "Guangdong": ["Guangzhou", "Shenzhen", "Zhuhai", "Dongguan"],
            "Zhejiang": ["Hangzhou", "Ningbo", "Wenzhou", "Shaoxing"],
            "Fujian": ["Fuzhou", "Xiamen", "Quanzhou", "Zhangzhou"],
            "Sichuan": ["Chengdu", "Mianyang", "Luzhou", "Nanchong"],
            "Jiangsu": ["Nanjing", "Suzhou", "Wuxi", "Changzhou"],
            "Shandong": ["Jinan", "Qingdao", "Yantai", "Weifang"],
            "Henan": ["Zhengzhou", "Luoyang", "Kaifeng", "Anyang"],
            "Hunan": ["Changsha", "Zhuzhou", "Xiangtan", "Yueyang"],
            "Hubei": ["Wuhan", "Huangshi", "Yichang", "Xiangyang"],
            "Anhui": ["Hefei", "Wuhu", "Bengbu", "Ma'anshan"],
            "Hebei": ["Shijiazhuang", "Tangshan", "Qinhuangdao", "Handan"],
            "Liaoning": ["Shenyang", "Dalian", "Anshan", "Fushun"],
            "Jilin": ["Changchun", "Jilin City", "Siping", "Yanji"],
            "Heilongjiang": ["Harbin", "Qiqihar", "Mudanjiang", "Jiamusi"],
            "Shaanxi": ["Xi'an", "Baoji", "Xianyang", "Weinan"],
            "Shanxi": ["Taiyuan", "Datong", "Changzhi", "Jincheng"],
            "Guangxi": ["Nanning", "Liuzhou", "Guilin", "Beihai"],
            "Yunnan": ["Kunming", "Dali", "Lijiang", "Qujing"],
            "Guizhou": ["Guiyang", "Zunyi", "Anshun", "Bijie"],
            "Inner Mongolia": ["Hohhot", "Baotou", "Ordos", "Chifeng"],
            "Tibet": ["Lhasa", "Shigatse", "Nyingchi", "Nagqu"],
            "Xinjiang": ["Urumqi", "Kashgar", "Hotan", "Korla"],
            "Ningxia": ["Yinchuan", "Shizuishan", "Wuzhong", "Guyuan"],
            "Qinghai": ["Xining", "Golmud", "Delingha", "Yushu"],
            "Gansu": ["Lanzhou", "Tianshui", "Jiuquan", "Zhangye"],
            "Hainan": ["Haikou", "Sanya", "Danzhou", "Qionghai"],
            "Hong Kong": ["Central", "Kowloon", "Tsuen Wan", "Tuen Mun"],
            "Macau": ["Macau Peninsula", "Taipa", "Cotai", "Coloane"],
        }

        for province_name, cities in data.items():
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

        self.stdout.write(self.style.SUCCESS("Database successfully populated with China's provinces and cities!"))
 