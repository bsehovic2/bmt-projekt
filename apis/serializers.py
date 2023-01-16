from rest_framework import serializers
from entries.models import Entry
from accounts.models import CustomUser


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('type', 'date', 'user',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'uid', 'credits',)
