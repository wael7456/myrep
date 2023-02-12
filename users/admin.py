from django.contrib import admin 
from .models import CustomUser 

from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
# Register your models here.

#class UserAdminConfig(UserAdmin):

   
   #list_display = ('email', 'username', 'first_name', 'is_active', 'is_admin')

admin.site.register (CustomUser )