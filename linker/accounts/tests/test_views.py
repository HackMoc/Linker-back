import json
from unittest.mock import Mock, patch
from django.http import JsonResponse

from django.test import Client, TestCase
from ..models import User
from django.urls import reverse
from ..services import user_create

class ViewTestCase(TestCase):

    def test_login_view_status_code_200(self):
        c = Client()
        response = c.post(reverse('accounts:login'), {'username': 'chris', 'password': 'test'})
        self.assertEqual(response.status_code, 200)

    def test_login_view_return_json(self):
        c = Client()
        response = c.post(reverse('accounts:login'), {'username': 'chris', 'password': 'test'})
        self.assertIsInstance(response, JsonResponse)

    def test_login_view_auth_successful_return_token(self):
        mock = Mock(return_value='879141ad-2b68-45a0-85c8-9a6d1cb25778')
        with patch('accounts.services.uuid4', mock):
            user_create(
                email='jhon@gmail.com',
                username='jhon',
                password='strong',
            )
        c = Client()
        response = c.post(reverse('accounts:login'), {'username': 'jhon', 'password': 'strong'})
        data = json.loads(response.content)
        self.assertEqual(data['token'], '879141ad-2b68-45a0-85c8-9a6d1cb25778')

    def test_login_view_auth_not_successful_return_token(self):
        c = Client()
        response = c.post(reverse('accounts:login'), {'username': 'jhon', 'password': 'strong'})
        data = json.loads(response.content)
        self.assertEqual(data['error'], 'User not found')

    def test_register_view_status_code_200(self):
        c = Client()
        response = c.post(
            reverse('accounts:register'),
            {'username':'jhon', 'email':'jhon@gmail.com', 'password':'strong'}
        )
        self.assertEqual(response.status_code, 200)

    def test_register_create_user(self):
        c = Client()
        response = c.post(
            reverse('accounts:register'),
            {'username':'jhon', 'email':'jhon@gmail.com', 'password':'strong'}
        )
        user = User.objects.get(username='jhon')
        self.assertIsNotNone(user)