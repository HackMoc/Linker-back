from django.contrib.auth.hashers import check_password
from django.test import TestCase

from ..models import User
from ..services import user_create


class ServicesTestCase(TestCase):

    def test_verifica_password_of_user(self):
        user_create(
            username='jhon',
            email='jhon@gmail.com',
            password='super strong pass',
        )
        user = User.objects.get(username='jhon')
        self.assertTrue(check_password('super strong pass', user.password))
