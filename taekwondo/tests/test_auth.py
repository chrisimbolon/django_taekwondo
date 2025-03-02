from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from taekwondo.models import Province, City, Belt, Coach
from django.utils.timezone import now  # Import this at the top


User = get_user_model()


class AuthIntegrationTest(TestCase):
    def setUp(self):
        """Create a test user"""
        self.username = "testuser"
        self.password = "testpassword123"
        self.user = User.objects.create_user(username=self.username, password=self.password)
        
        # Create test Province, City, and Belt
        self.province = Province.objects.create(province_name="New York", country="US")
        self.city = City.objects.create(city_name="Brooklyn", province=self.province)
        self.belt = Belt.objects.create(rank_name="Black Belt", rank_level=1, is_black_belt=True)

        self.coach = Coach.objects.create(
            full_name="Test Coach",
            registration_number="12345",
            place_of_birth="Brooklyn",
            date_of_birth="1990-01-01",
            dojang_name="NYC Taekwondo",
            sex="male",
            country="US",
            province=self.province,
            city=self.city,
            status="active",
            belt=self.belt,
            phone_number="1234567890",
            email="johndoe@example.com",
            input_date=now().date(),
            manager=self.user,  # Assign the test user as the manager
        )

    def test_signup_view(self):
        """Test user signup"""
        response = self.client.post(reverse("signup"), {
            "username": "newuser",
            "password1": "StrongPassword123!",
            "password2": "StrongPassword123!"
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful signup
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_login_view_success(self):
        """Test login with correct credentials"""
        response = self.client.post(reverse("login"), {
            "username": self.username,
            "password": self.password
        })
        self.assertEqual(response.status_code, 302)  # Should redirect to coaches-list
        self.assertRedirects(response, reverse("coaches-list"))

    def test_login_view_invalid_credentials(self):
        """Test login with incorrect credentials"""
        response = self.client.post(reverse("login"), {
            "username": self.username,
            "password": "wrongpassword"
        }, follow=True)  # Follow redirects to see where it lands

        print(response.request["PATH_INFO"])
        print(response.request["QUERY_STRING"])
        
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, "coaches.html")  
        
        messages = list(get_messages(response.wsgi_request))
        print(f"Messages count: {len(messages)}")
        for msg in messages:
            print(f"Message: {msg}")

        self.assertTrue(any("Invalid username or password." in str(msg) for msg in messages))


    def test_unauthenticated_user_gets_redirected(self):
        """Test that an unauthenticated user attempting to access a protected view gets a 302 redirect."""
        response = self.client.get(reverse("detail", kwargs={"pk": 1}))  # Random ID
        self.assertEqual(response.status_code, 302)  # Should redirect to login page

    def test_logout_view(self):
        """Test user logout"""
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse("logout"))  # Use POST instead of GET
        self.assertEqual(response.status_code, 302)  # Should redirect after logout
        self.assertRedirects(response, reverse("logged_out"))


    def test_login_view_ajax_success(self):
        """Test AJAX login success"""
        response = self.client.post(
            reverse("login"),
            {"username": self.username, "password": self.password},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest"
        )
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"success": True})

    def test_login_view_ajax_fail(self):
        """Test AJAX login failure"""
        response = self.client.post(
            reverse("login"),
            {"username": self.username, "password": "wrongpass"},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest"
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("errors", response.json())

    def test_get_csrf_token(self):
        response = self.client.get(reverse("get_csrf_token"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("csrf_token", response.json())

    def test_unauthenticated_user_redirects_to_coaches_list(self):
        """Test that an unauthenticated user is redirected to the coaches list when trying to access a protected view."""
        response = self.client.get(reverse("detail", kwargs={"pk": self.coach.pk}), follow=True)

        print(f"Redirect chain: {response.redirect_chain}")  # Debugging
        expected_redirect_url = reverse("coaches-list")  # If your app redirects there

        self.assertRedirects(response, expected_redirect_url)

    def test_authenticated_user_can_access_protected_view(self):
        """Test that a logged-in user can access a protected view"""
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse("detail", kwargs={"pk": self.coach.pk}))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "detail.html")
        self.assertContains(response, "Test Coach")  # Ensure the coach name appears in the response