from accounts.services import user_auth, user_create

from django.http import JsonResponse
from django.views import View


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


class RegisterView(View):
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_create(username, email, password)
        data = {}
        return JsonResponse(data, status=200)
