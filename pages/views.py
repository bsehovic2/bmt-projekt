# pages/views.py
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class ProfilePageView(TemplateView):  # new
    template_name = "profile.html"
