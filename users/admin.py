from django.contrib import admin
from django.contrib.admin import register

from users.models import CustomUser


@register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
