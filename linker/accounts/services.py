from accounts.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ObjectDoesNotExist
from uuid import uuid4


def user_auth(username, password):
    try:
        user = User.objects.get(
            username=username,
        )
        if check_password(password, user.password):
            return user
    except ObjectDoesNotExist:
        pass
    return None


def user_create(username, email, password):
    token = uuid4()
    User.objects.create(
        username=username,
        email=email,
        password=make_password(password),
        token=token,
    )
