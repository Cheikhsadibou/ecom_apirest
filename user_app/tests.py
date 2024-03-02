from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

class RegistrationTestCase(APITestCase):
    # def setUp(self):
    def test_registration(self):
        data = {
            'username': 'testcase',
            'email': 'testcase@gmail.com',
            'password': 'password@123',
            'password2': 'password@123'
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
class LoginLogoutTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="password@123")
    def test_login(self):
        data = {
            "username": "example",
            "password": "password@123"
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data['username'], data['username'])
        # self.assertEqual(response.data['email'], data['email'])
        # self.assertEqual(response.data['password'], data['password'])
        # self.assertEqual(response.data['is_staff'], False)
        # self.assertEqual(response.data['is_superuser'], False)
        # self.assertEqual(response.data['is_active'], True)
        # self.assertEqual(response.data['date_joined'], None)

    def test_logout(self):
        self.token = Token.objects.get(user__username="example")
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token.key)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
