from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from django.db.models import Q
from .utils import normalize_phone_number, normalize_email

User = get_user_model()


class EmailPhoneAuthenticationBackend(object):
    @staticmethod
    def authenticate(request, username=None, password=None):
        try:
            user = User.objects.get(
                Q(phone_number=normalize_phone_number(username))
                | Q(email=normalize_email(username))
            )

        except User.DoesNotExist:
            return None

        if user and check_password(password, user.password):
            return user

        return None

    @staticmethod
    def get_user(user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
