from django.contrib import admin
from .models import customer_profile

# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
     pass

admin.site.register(customer_profile)