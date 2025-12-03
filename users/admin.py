from django.contrib import admin
from .models import UserExtends
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserExtendsAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'last_name', 'first_name',  'othername', 'phone_number')

admin.site.register(UserExtends, UserExtendsAdmin)