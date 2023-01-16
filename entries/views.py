from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Entry
from rest_framework import generics
from apis.serializers import EntrySerializer


class EntryListView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = "home.html"


class EntryDetailView(LoginRequiredMixin, DetailView):  # new
    model = Entry
    template_name = 'entry.html'


class EntryAPIListView(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
