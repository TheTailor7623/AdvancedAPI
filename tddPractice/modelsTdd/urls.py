from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard.as_view()),
    # path("profile/", views.profile.as_view()),
    # path("profile/<int:profile_id>", views.profile.as_view()),
]
