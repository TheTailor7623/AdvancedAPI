from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class dashboard(APIView):
    """Displays a list of endpoints for this API"""

    def get(self, request, format=None):
        """This returns the list when a get request is made"""
        list_of_urls = [
            "http://127.0.0.1:8000/api/user/profile",
            "http://127.0.0.1:8000/api/user/registration",
            "http://127.0.0.1:8000/api/user/login",
        ]
        return Response({
            "List of API endpoints":list_of_urls,
        })