from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages


User = get_user_model()


class AuthIntegrationTest(TestCase):
    def setUp(self):
        """Create a test user"""
        self.username = "testuser"
        self.password = "testpassword123"
        self.user = User.objects.create_user(username=self.username, password=self.password)
        

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



    def test_login_required_redirect(self):
        """Test that an unauthenticated user is redirected when trying to access a protected view"""
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

