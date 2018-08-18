from django.test import Client, TestCase
from .models import User
from django.urls import reverse

class ModelsTestCase(TestCase):

    def test_model_instance(self):
        username = User()
        self.assertIsInstance(username, User)

    def teste_field_not_blank(self):
        user = User.objects.create(
            email='jhon@gmail.com',
        )
        user.save()
        self.assertNotEqual(user.username, None)

    def test_verifica_password_of_user(self):
        user = User.objects.create(
            username='jhon',
            email='jhon@gmail.com',
        )
        username.save()
class ViewTestCase(TestCase):

        self.assertNotEqual(username.first_name, None)
    def test_login_view_status_code_200(self):
        c = Client()
        response = c.post(reverse('accounts:login'), {'username': 'chris', 'password': 'test'})
        self.assertEqual(response.status_code, 200)
