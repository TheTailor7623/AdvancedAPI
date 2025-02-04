from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard.as_view()),
    path("user/registration/", views.RegisterUserView.as_view()),
    path("user/login/", views.LoginUserView.as_view()),
]
