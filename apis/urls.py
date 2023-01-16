from django.urls import path
from entries.views import EntryAPIListView, EntryAPIDetailView
f#rom accounts.views import

app_name = 'entries'
urlpatterns = [
    path('entries/<pk>/', EntryAPIDetailView.as_view(), name='entry_detail'),
    path('entries/', EntryAPIListView.as_view(), name='entry_list'),
    #path('users/<pk>/', UserAPIDetailView.as_view(), name='entry_detail'),
    #path('users/', UserAPIListView.as_view(), name='entry_list'),
]
