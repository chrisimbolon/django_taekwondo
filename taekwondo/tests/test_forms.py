from django.test import TestCase
from taekwondo.forms import CoachForm
from taekwondo.models import Province, City, Belt, Coach
from django.contrib.auth.models import User
from django.utils.timezone import now

class CoachFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.province = Province.objects.create(province_name="Ontario", country="CA")
        self.city = City.objects.create(city_name="Toronto", province=self.province)
        self.belt = Belt.objects.create(rank_name="Black Belt", rank_level=5, is_black_belt=True)

    def test_valid_form(self):
        form_data = {
            "registration_number": "12345",
            "full_name": "John Doe",
            "place_of_birth": "Brooklyn",
            "date_of_birth": "01-01-1990",  # DD-MM-YYYY format
            "dojang_name": "NYC Taekwondo",
            "sex": "male",
            "country": "CA",
            "province": self.province.id,
            "city": self.city.id,
            "status": "active",
            "belt": self.belt.id,
            "bio": "Experienced coach",
            "achievements": "Multiple championships",
            "phone_number": "1234567890",
            "email": "johndoe@example.com",
        }

        form = CoachForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_invalid_date_format(self):
        """Ensure incorrect date format fails validation."""
        form_data = {
            "registration_number": "12345",
            "full_name": "John Doe",
            "place_of_birth": "Brooklyn",
            "date_of_birth": "1990-01-01",  # Wrong format (should be DD-MM-YYYY)
            "dojang_name": "NYC Taekwondo",
            "sex": "male",
            "country": "CA",
            "province": self.province.id,
            "city": self.city.id,
            "status": "active",
            "belt": self.belt.id,
            "bio": "Experienced coach",
            "achievements": "Multiple championships",
            "phone_number": "1234567890",
            "email": "johndoe@example.com",
        }

        form = CoachForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("date_of_birth", form.errors)  # Check if the error is raised


