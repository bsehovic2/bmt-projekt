from django.contrib import admin
from .models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'type',]



admin.site.register(Entry, EntryAdmin)
