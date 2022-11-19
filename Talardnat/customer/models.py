from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

class Profile(models.Model):
    customer = models.ForeignKey(User, related_name="profile", on_delete=models.CASCADE, unique=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    state = models.CharField(max_length=40, null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=20,null=True, blank=True)

    def __str__(self):
        return f"{self.customer}"



# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     try:
#         instance.profile.save()
#     except ObjectDoesNotExist:
#         Profile.objects.create(customer=instance)