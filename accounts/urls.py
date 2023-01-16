# accounts/urls.py
from django.urls import path, include
from .views import SignupPageView

urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
    path('api/', include('apis.urls', namespace='api')),
]
