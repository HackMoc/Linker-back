from django.test import TestCase
from django import forms
from accounts.forms import CredentialsForm 


class FormTestCase(TestCase):
    def test_form_is_instance(self):
        form = CredentialsForm()
        self.assertIsInstance(form, forms.Form)

    def test_form_without_username_is_not_valid(self):
        data_form = {
            'email': 'jhon@gmail.com',
            'password': 'super strong pass',
        }
        form = CredentialsForm(data_form)
        self.assertFalse(form.is_valid())
        
    def test_form_email_field_is_not_valid(self):
        data_form = {
            'username': 'jhon',
            'email': 'lets go fellas',
            'password': 'super strong pass',
        }
        form = CredentialsForm(data_form)
        self.assertFalse(form.is_valid())
        
    def test_form_user_space_sensitive(self):
        data_form = {
            'username': '    jhon',
            'email': 'jhon@gmail.com',
            'password': 'super strong pass',
        }
        form = CredentialsForm(data_form)
        form.is_valid()
        self.assertEqual(form.cleaned_data['username'], 'jhon')