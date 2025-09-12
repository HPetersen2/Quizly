from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status


class LogoutTest(APITestCase):

    def setUp(self):
        self.login_url = reverse('login-view')
        self.logout_url = reverse('token-blacklist')

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


    def test_logout_success(self):
        response = self.client.post(
            self.logout_url,
            {},
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access_token', response.cookies)
        self.assertEqual(response.cookies['access_token'].value, '')
        self.assertIn('refresh_token', response.cookies)
        self.assertEqual(response.cookies['refresh_token'].value, '')
        self.assertJSONEqual(response.content, {
            "detail": "Log-Out successfully! All Tokens will be deleted. Refresh token is now invalid."
        })


    def test_logout_without_token(self):
        response = self.client.post(self.logout_url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertJSONEqual(response.content, {
            "detail": "Authentication credentials were not provided."
        })