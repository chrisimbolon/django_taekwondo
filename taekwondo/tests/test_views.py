from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from taekwondo.models import Coach, Province, City 
from datetime import date
from taekwondo.models import Belt  # Import Belt

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')

    # Fix: Use the correct field name `province_name`
        self.province = Province.objects.create(province_name="California", country="US")  

    # Fix: Use the correct field name `city_name`
        self.city = City.objects.create(city_name="Los Angeles", province=self.province)

        self.belt = Belt.objects.create(rank_name="Black Belt", rank_level=1, is_black_belt=True)
        # Create a test coach
        self.coach = Coach.objects.create(
            full_name='John Doe',
            country='US',
            phone_number='1234567890',
            date_of_birth="1990-01-01",  # <-- Add a valid date here
            manager=self.user,
            belt=self.belt  # Assign the belt here
    )

    def test_home_page_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, "Effortlessly Manage Your Taekwondo Coaches")

    def test_coach_list_view(self):
        response = self.client.get(reverse('coaches-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'coaches.html')
        self.assertContains(response, self.coach.full_name)

    def test_coach_detail_view_requires_login(self):
        response = self.client.get(reverse('detail', kwargs={'pk': self.coach.pk}))
        self.assertEqual(response.status_code, 302)  # Redirect to login

        # Now log in and try again
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('detail', kwargs={'pk': self.coach.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail.html')
        self.assertContains(response, self.coach.full_name)

    def test_create_coach_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('create'), {
            'full_name': 'New Coach',
            'registration_number': '654321',
            'country': 'US',  # Must match allowed choices
            'province': self.province.id,  # Use ID
            'city': self.city.id,
            'phone_number': '9876543210',
            'place_of_birth': 'Some Place',
            'date_of_birth': '01-01-1990',
            'dojang_name': 'Some Dojang',
            'sex': 'male',  # Assuming this is a choice field
            'status': 'active',  # Assuming it's a choice field
            'belt': self.belt.id,  # Add this line
            'email': 'coach@example.com',
            'manager': self.user.id  # Manager is required
        })

    # Print errors if the form fails
        if response.status_code == 200:
             print(response.context.get('form').errors)
             print(response.context['form']['belt'].field.choices)

        self.assertEqual(response.status_code, 302)  # Redirect after success


    def test_update_coach_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('update', kwargs={'pk': self.coach.pk}), {
            'full_name': 'Updated Coach',
            'registration_number': '123456',
            'country': 'US',  # Must match allowed choices
            'province': self.province.id,  # Use ID
            'city': self.city.id,  # Use ID
            'phone_number': '1234567890',
            'place_of_birth': 'Updated Place',
            'date_of_birth': '01-01-1990',
            'dojang_name': 'Updated Dojang',
            'sex': 'male',
            'status': 'active',
            'belt': self.belt.id,  # Add this line
            'email': 'updatedcoach@example.com',
            'manager': self.user.id
        })
    
    # Print errors if the form fails
        if response.status_code == 200:
            print(response.context.get('form').errors)
            print(response.context['form']['belt'].field.choices)


        self.assertEqual(response.status_code, 302)  # Redirect after success

        self.coach.refresh_from_db()
        self.assertEqual(self.coach.full_name, 'Updated Coach')  # Fix this assertion


    def test_ajax_login_view(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'password'
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': True})
