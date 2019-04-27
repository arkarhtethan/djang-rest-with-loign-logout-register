from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):

	list_display = ('username','email','name',"is_staff","is_active")

	list_filter = ("is_staff","is_active")

	list_editable = ("email","name")


admin.site.register(CustomUser, CustomUserAdmin)
