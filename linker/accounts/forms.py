from django import forms


class CredentialsForm(forms.Form):
    username = forms.CharField(max_length=16)
    email = forms.EmailField(max_length=255)
    password = forms.CharField(max_length=255)
