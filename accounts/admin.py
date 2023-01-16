# accounts/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'uid', 'is_superuser', 'first_name', 'last_name'] # new
    fieldsets = UserAdmin.fieldsets + ( # new
        (None, {'fields': ('uid', 'credits')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + ( # new
        (None, {'fields': ('uid', 'credits')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
