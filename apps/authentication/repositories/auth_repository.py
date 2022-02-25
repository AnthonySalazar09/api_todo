

from datetime import datetime
from django.contrib.auth.models import User


class AuthRepository():

    def get_user_by_id(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    def get_user_by_email(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

    def get_user_by_username(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    def create_user(self, data):
        user = User(
            username=data.get('username'),
            first_name='',
            last_name='',
            email='',
            password=data.get('password'),
            is_staff=False,
            is_active=True,
            is_superuser=False,
            )
        user.save()
        return user
