# pages/urls.py
from django.urls import path

from .views import HomePageView, ProfilePageView

urlpatterns = [
    path("profile/", ProfilePageView.as_view(), name="profile"),
    path("", HomePageView.as_view(), name="home"),
]