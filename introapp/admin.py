from django.contrib import admin
from django.conf import settings

from .models import Intro_BW

admin.site.register(Intro_BW)

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

UserAdmin.list_display = ('username', 
                          'email', 
                        #   'last_name', 
                        #   'first_name', 
                          'date_joined',
                          'is_active',
                          'is_staff',
                          'is_superuser')
                          
UserAdmin.list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)