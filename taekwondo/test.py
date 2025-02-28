from django.test import TestCase
from .models import Province, City, Belt, Coach
from django.contrib.auth.models import User
from django.utils.timezone import now

class ProvinceModelTest(TestCase):
    def test_create_province(self):
        province = Province.objects.create(province_name="Ontario", country="CA")
        self.assertEqual(str(province), "Ontario, CA")

class CityModelTest(TestCase):
    def test_create_city(self):
        province = Province.objects.create(province_name="California", country="US")
        city = City.objects.create(city_name="Los Angeles", province=province)
        self.assertEqual(str(city), "Los Angeles, California, US")

class BeltModelTest(TestCase):
    def test_create_belt(self):
        belt = Belt.objects.create(rank_name="Yellow Belt", rank_level=2, is_black_belt=False)
        self.assertEqual(str(belt), "Yellow Belt")

class CoachModelTest(TestCase):
    def test_create_coach(self):
        user = User.objects.create(username="testuser")
        province = Province.objects.create(province_name="New York", country="US")
        city = City.objects.create(city_name="NYC", province=province)
        belt = Belt.objects.create(rank_name="Black Belt", rank_level=5, is_black_belt=True)
        
        coach = Coach.objects.create(
            manager=user,
            registration_number="12345",
            full_name="John Doe",
            place_of_birth="Brooklyn",
            date_of_birth="1990-01-01",
            dojang_name="NYC Taekwondo",
            sex="male",
            country="US",
            province=province,
            city=city,
            status="active",
            belt=belt,
            phone_number="1234567890",
            email="johndoe@example.com",
            input_date=now().date()
        )

        self.assertEqual(str(coach), "John Doe")
