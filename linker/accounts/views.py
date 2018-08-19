from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from accounts.services import user_auth

class LoginView(View):
    def post(self, request):
        data = {}
        user = user_auth(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
        )
        if user:
            data['token'] = user.token
        else:
            data['error'] = 'User not found'
        return JsonResponse(data, status=200)

