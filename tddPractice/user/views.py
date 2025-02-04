from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView, Response
from rest_framework.settings import api_settings

from django.contrib.auth import authenticate
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from user import serializers, permissions

# Create your views here.
class RegisterUserView(APIView):
    """View handling the registration of users"""
    serializer_class = serializers.UserRegistrationSerializer

    def get(self, request, format=None):
        """This asks user to make a POST request to register"""
        output = {
            "Message":"❌ Please make a POST request to register!"
        }
        return Response(
            output,
            status=status.HTTP_400_BAD_REQUEST
        )

    def post(self, request, format=None):
        """Handles POST requests made to the registration endpoint view"""
        serialized_data = self.serializer_class(data=request.data)

        if serialized_data.is_valid():
            new_user = serialized_data.save()
            output = {
                "Message":"✅ User has been created successfully!",
                "Name":new_user.name,
                "Email":new_user.email,
            }

            return Response(
                output,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serialized_data.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

class LoginUserView(ObtainAuthToken):
    """Authenthicates and provides users with a token"""

    def post(self, request, format=None):
        """Authenticates user and returns token"""
        login_data = {
            "email":request.data.get("email"),
            "password":request.data.get("password"),
        }

        user = authenticate(**login_data)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            output = {
                "Message":"✅ Login successful!",
                "Token":token.key,
            }
            return Response(
                output,
                status=status.HTTP_200_OK
            )
        output = {
            "Message":"❌ Login unsuccessful!",
            "Information":user.errors,
        }
        return Response(
            output,
            status=status.HTTP_400_BAD_REQUEST
        )

class UserProfileView(APIView):
    """Handles a user profile"""
    serializer_class = serializers.UserProfileSerializer
    permission_classes = (permissions.UpdateOwnProfile, IsAuthenticated)
    authentication_classes = (TokenAuthentication,)

    def get(self, request, format=None):
        """Return user details"""
        serialized_data = self.serializer_class(request.user)
        return Response(serialized_data.data, status=status.HTTP_200_OK)