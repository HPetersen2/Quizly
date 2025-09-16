# from django.urls import reverse
# from django.contrib.auth.models import User
# from rest_framework.test import APITestCase
# from rest_framework import status

# class CreateQuizTest(APITestCase):
#     def setUp(self):
#         self.login_url = reverse('login-view')
#         self.quiz_url = reverse('create-quiz')
#         self.username = 'newuser'
#         self.password = 'newpassword123'
#         self.user = User.objects.create_user(
#             username=self.username,
#             password=self.password,
#             email='newuser@test.de'
#         )
#         self.user_data = {
#             'username': self.username,
#             'password': self.password
#         }

#         response = self.client.post(self.login_url, {
#             'username': self.username,
#             'password': self.password
#         }, format='json')

#         self.client.cookies['access_token'] = response.cookies.get('access_token').value

#     def test_create_quiz(self):
#         data = {
#             "url": "https://www.youtube.com/watch?v=u-buCC1LWr8"
#         }
#         response = self.client.post(self.quiz_url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         excepted_fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'video_url', 'questions']
#         for field in excepted_fields:
#             self.assertIn(field, response.data)

#     def test_create_quiz_with_invalid_url(self):
#         data = {
#             "url": "https://www.youtube.com/watch?v=u-LWr8"
#         }
#         response = self.client.post(self.quiz_url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_create_quiz_without_login(self):
#         self.client.cookies['access_token'] = ""
#         data = {
#             "url": "https://www.youtube.com/watch?v=u-buCC1LWr8"
#         }
#         response = self.client.post(self.quiz_url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)