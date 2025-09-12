from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

class RefreshToken(APITestCase):
    def setUp(self):
        self.login_url = reverse('login-view')
        self.refresh_url = reverse('token-refresh')

        self.username = 'testuser'
        self.password = 'testpassword123'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
            email='test@test.de'
        )

        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password
        }, format='json')

        self.access_token = response.cookies.get('access_token').value
    

    def test_refresh_token_success(self):
        response = self.client.post(self.refresh_url, {}, format='json')
        new_access_token = response.cookies['access_token'].value
        self.assertNotEqual(self.access_token, new_access_token)
        self.assertJSONEqual(response.content, {
            "detail": "Token refreshed",
            "access": "new_access_token"
        })


    def test_refresh_token_without_cookie(self):
        client = self.client_class()
        response = client.post(self.refresh_url, {}, format='json')
        self.assertIn(response.status_code, [status.HTTP_400_BAD_REQUEST, status.HTTP_401_UNAUTHORIZED])