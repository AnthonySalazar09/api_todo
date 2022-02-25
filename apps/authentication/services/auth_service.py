from datetime import datetime
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

from apps.authentication.repositories.auth_repository import AuthRepository


class AuthService():

    def general_auth(self, data):
        username = data.get('username')
        user = AuthRepository().get_user_by_username(username)
        if user:
            is_pw_valid = self.login(data, user)
        else:
            user, is_pw_valid = self.signup(data)
        user.last_login = datetime.now()
        user.save()
        return user, is_pw_valid

    def login(self, data, user):
        is_pw_valid = check_password(data.get('password'), user.password)
        return is_pw_valid

    def signup(self, data):
        data['password'] = make_password(data['password'])
        user = AuthRepository().create_user(data)
        return user, True
