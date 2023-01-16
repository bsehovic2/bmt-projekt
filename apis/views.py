from rest_framework import generics
from entries.models import Entry
from apis.serializers import EntrySerializer


class EntryListView(generics.ListAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryDetailView(generics.RetrieveAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
