# entries/urls.py
from django.urls import path
from .views import EntryListView, EntryDetailView

urlpatterns = [
    path('<int:pk>/', EntryDetailView.as_view(), name='entry'),
    path('', EntryListView.as_view(), name='entry_list'),
]