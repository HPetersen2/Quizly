from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

class RegisterTest(APITestCase):

    def setUp(self):
        self.url = reverse('register-view')
        self.user_data = {
            'username': 'newuser',
            'password': 'newpassword123',
            'email': 'newuser@test.de'
        }
        User.objects.create_user(username='testuser', password='testpassword', email='test@test.de')


    def test_register(self):
        response = self.client.post(self.url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='newuser').exists())
        self.assertJSONEqual(response.content, {
            "detail": "User created successfully!"
        })


    def test_register_existing_username(self):
        data = {
            'username': 'testuser',
            'password': 'somepassword',
            'email': 'other@test.de'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertJSONEqual(response.content, {
            "username": [
                "A user with that username already exists."
            ]
        })


    def test_register_invalid_email(self):
        data = {
            'username': 'anotheruser',
            'password': 'somepassword',
            'email': 'not-an-email'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertJSONEqual(response.content, {
            "email": [
                "Enter a valid email address."
            ]
        })


    def test_register_missing_password(self):
        data = {
            'username': 'usernopw',
            'email': 'usernopw@test.de'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertJSONEqual(response.content, {
            "password": [
                "This field is required."
            ]
        })


    def test_register_empty_password(self):
        data = {
            'username': 'usernopw',
            'email': 'usernopw@test.de',
            'password': ''
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertJSONEqual(response.content, {
            "password": [
                "This field may not be blank."
            ]
        })