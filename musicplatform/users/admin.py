from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
class CustomUserAdmin(UserAdmin):
    fieldsets=(*UserAdmin.fieldsets,(
        'Bio',
        {
            'fields':('bio',)
        }
    ))
admin.site.register(User,CustomUserAdmin)