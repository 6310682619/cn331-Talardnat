# Generated by Django 4.1.3 on 2022-11-12 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.CharField(blank=True, max_length=150, null=True)),
                ("city", models.CharField(blank=True, max_length=40, null=True)),
                ("state", models.CharField(blank=True, max_length=40, null=True)),
                ("zip", models.IntegerField(blank=True, null=True)),
                ("phone", models.IntegerField(blank=True, null=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                        unique=True,
                    ),
                ),
            ],
        ),
    ]
