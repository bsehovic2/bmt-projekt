from rest_framework import serializers
from entries.models import Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('type', 'date', 'user',)
