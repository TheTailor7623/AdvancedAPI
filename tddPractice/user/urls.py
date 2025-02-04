from django.urls import path, include
from user import views

urlpatterns = [
    path("registration/", views.RegisterUserView.as_view(), name="register"),
    path("login/", views.LoginUserView.as_view(), name="login"),
    path("profile/", views.UserProfileView.as_view(), name="profile"),
]
