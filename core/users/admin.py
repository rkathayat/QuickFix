from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Role", {"fields": ("is_customer", "is_mechanic")}),
    )
    list_display = ("username", "email", "is_customer", "is_mechanic", "is_staff")

admin.site.register(User, UserAdmin)
