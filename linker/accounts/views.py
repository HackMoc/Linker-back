from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class LoginView(View):
    def post(self, request):
        return HttpResponse('result', status=200)

