from django.conf import settings

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from apps.authentication.services.auth_service import AuthService
from apps.authentication.serializers.auth_serializer import UserSerializer



class AuthController(viewsets.ViewSet):
    """
    A Controller for Todo Tasks/Folders.
    """

    def login_signup(self, request):
        data = request.data
        user, is_pw_valid = AuthService().general_auth(data)
        if not is_pw_valid:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


