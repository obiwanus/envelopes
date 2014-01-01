from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User, check_password


class AuthBackend(ModelBackend):
    def authenticate(self, username=None, password=None):
        login_valid = (settings.ADMIN_LOGIN == username)
        pwd_valid = password == settings.ADMIN_PASSWORD
        if login_valid and pwd_valid:
            user = User.objects.get(username=username)
            return user
        return None


class AuthEmailBackend(ModelBackend):
    def authenticate(self, email=None, password=None):
        user = User.objects.get(email=email)
        if user:
            pwd_valid = check_password(password, user.password)
            if pwd_valid:
                return user
        return None