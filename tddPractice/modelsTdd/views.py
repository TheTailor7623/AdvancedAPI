from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken

from modelsTdd import models, serializers

# Create your views here.
class dashboard(APIView):
    """Displays a list of endpoints for this API"""

    def get(self, request, format=None):
        """This returns the list when a get request is made"""
        list_of_urls = [
            "http://127.0.0.1:8000/api/user/YOUR_PROFILE",
            "http://127.0.0.1:8000/api/user/registration",
            "http://127.0.0.1:8000/api/user/login",
        ]
        return Response({
            "List of API endpoints":list_of_urls,
        })

class RegisterUserView(APIView):
    """Lets the user interact with out API"""
    serializer_class = serializers.UserProfileSerializer

    def get(self, request):
        output_data = {
            "Message": "Please POST your registration details to this endpoint.",
        }
        return Response(
            output_data,
            status=status.HTTP_200_OK,
        )

    def post(self, request, format=None):
        """Handles POST requests made by the user"""
        serialized_data = self.serializer_class(data=request.data)

        if serialized_data.is_valid():
            user_registered = serialized_data.save()
            output_data = {
                "Message":"User created successfully✅",
                "Email":user_registered.email,
                "Name":user_registered.name,
            }
            return Response(
                output_data,
                status=status.HTTP_201_CREATED
            )

        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginUserView(ObtainAuthToken):
    """Handle creating user authenthication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
