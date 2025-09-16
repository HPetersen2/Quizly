from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

class CreateQuizTest(APITestCase):
    def setUp(self):
        self.login_url = reverse('login-view')
        self.quiz_url = reverse('create-quiz')
        self.quiz_list_url = reverse('quiz-list')
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

        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password
        }, format='json')

        self.client.cookies['access_token'] = response.cookies.get('access_token').value

        data = {
            "url": "https://www.youtube.com/watch?v=u-buCC1LWr8"
        }

        created_quiz = self.client.post(self.quiz_url, data, format='json')

    def test_get_quizzes(self):
        response = self.client.get(self.quiz_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)