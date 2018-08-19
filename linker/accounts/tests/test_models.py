from django.test import Client, TestCase
from ..models import User
from django.contrib.auth.hashers import check_password, make_password
from django.urls import reverse
from django.db import IntegrityError

class ModelsTestCase(TestCase):

    def test_model_instance(self):
        username = User()
        self.assertIsInstance(username, User)

    def test_verifica_password_of_user(self):
        user = User.objects.create(
            username='jhon',
            email='jhon@gmail.com',
        )
        password = 'super strong pass'
        user.password = make_password(password)
        user.save()
        self.assertTrue(check_password(password, user.password))

    def test_assert_token_valid(self):
        user = User.objects.create(
            email='jhon@gmail.com',
            username='jhon',
            password='strong',
            token='879141ad-2b68-45a0-85c8-9a6d1cb25778'
        )
        self.assertEqual(user.token, '879141ad-2b68-45a0-85c8-9a6d1cb25778')

    def test_create_duplicated_user(self):
        User.objects.create(
            email='jhon@gmail.com',
            username='jhon',
        )
        with self.assertRaises(IntegrityError):
            User.objects.create(
                email='jhon@gmail.com',
                username='jhon',
            )