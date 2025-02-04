from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.dashboard.as_view()),
    path("user/", include("user.urls")),
]
