from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

class RegisterTest(APITestCase):

    def setUp(self):
        self.url = reverse('login-view')
        self.username = 'newuser'
        self.password = 'newpassword123'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
            email='newuser@test.de'
        )
        self.user_data = {
            'username': self.username,
            'password': self.password
        }


    def test_login(self):
        response = self.client.post(self.url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access_token', response.cookies)
        self.assertIn('refresh_token', response.cookies)
        self.assertJSONEqual(response.content, {
            "detail": "Login successfully!",
            "user": {
                "id": self.user.id,
                "username": self.username,
                "email": self.user.email
            }
        })


    def test_login_false_username(self):
        data = {
            'username': 'michwirdesniegeben',
            'password': self.password,
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn('access_token', response.cookies)
        self.assertNotIn('refresh_token', response.cookies)
        self.assertJSONEqual(response.content, {
            "detail": "No active account found with the given credentials"
        })


    def test_login_false_password(self):
        data = {
            'username': self.username,
            'password': 'somepassword'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn('access_token', response.cookies)
        self.assertNotIn('refresh_token', response.cookies)
        self.assertJSONEqual(response.content, {
            "detail": "No active account found with the given credentials"
        })


    def test_login_missing_password(self):
        data = {
            'username': self.username,
            'password': ''
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('access_token', response.cookies)
        self.assertNotIn('refresh_token', response.cookies)
        self.assertJSONEqual(response.content, {
            'password': ['This field may not be blank.']
        })

    
    def test_login_missing_username(self):
        data = {
            'username': '',
            'password': self.password
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('access_token', response.cookies)
        self.assertNotIn('refresh_token', response.cookies)
        self.assertJSONEqual(response.content, {
            'username': ['This field may not be blank.']
        })
