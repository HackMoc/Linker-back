from django.test import Client, TestCase
from .models import User

class ModelsTestCase(TestCase):

    def test_model_instance(self):
        username = User()

        self.assertIsInstance(username, User)

    def teste_field_not_blank(self):
        username = User.objects.create(
            last_name='mcdonald',
            username='jhon',
            email='jhon@gmail.com',
        )
        username.save()

        self.assertNotEqual(username.first_name, None)
