from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    customer = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE, default=1)
    address = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    state = models.CharField(max_length=40, null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.customer}"

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(customer=instance)
    instance.profile.save()