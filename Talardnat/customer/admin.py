from django.contrib import admin
from .forms import RegisterForm

# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
     list_display = ["firstname", "lastname", "address", "username", "email", "password1", "password2"]

#admin.site.register([RegisterForm], SignUpAdmin)