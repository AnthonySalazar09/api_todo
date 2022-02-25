from django.urls import path

from apps.authentication.controllers.auth_controller import AuthController


urlpatterns = [
    path('signup/', AuthController.as_view(
        {'post': 'login_signup'}), name='signup'),
]
