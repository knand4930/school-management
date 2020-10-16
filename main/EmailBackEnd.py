from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend, UserModel
from django.contrib.auth.models import User
from django.db.models import Q


class EmailBackEnd(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
            user = UserModel.objects.get(email=username)
        except UserModel.DoseNotExist:
            return None
        else:
            if user.check_password(password):
                return user
            return None
