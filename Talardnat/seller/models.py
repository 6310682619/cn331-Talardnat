from django.db import models
from django.contrib.auth.models import User

class seller_detail(models.Model):
    sname = models.ForeignKey(User, on_delete=models.CASCADE, null=True , related_name="sname")

    def __str__(self):
        return f"{self.sname}"