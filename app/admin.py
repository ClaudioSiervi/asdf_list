from django.contrib import admin

from app.models.user import User, Family

admin.site.register(User)

admin.site.register(Family)