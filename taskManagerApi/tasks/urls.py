from django.urls import path, include
from tasks import views

urlpatterns = [
    path("", views.home, name="home")
]
