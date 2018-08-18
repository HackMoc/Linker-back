from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from accounts.models import User

class LoginView(View):
    def post(self, request):
        try:
            user = User.objects.get(
                username=request.POST.get('username'),
                password=request.POST.get('password'),
            )
            data = user.token
        except:
            data = 'User not found'
        return HttpResponse(data, content_type="text/plain", status=200)

