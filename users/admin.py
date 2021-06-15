from users.models import User
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin



class CustomUserAdmin(UserAdmin):
    list_display=["first_name", "last_name"]
    # fields=["first_name", "last_name", "email", "username", "password", "gender", "birthday"]
    # ...

admin.site.register(User, CustomUserAdmin)
