# Generated by Django 4.1.1 on 2022-11-19 15:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("myshop", "0003_myorder_confirmpay_myorder_confirmrecieved"),
    ]

    operations = [
        migrations.AddField(
            model_name="myorder",
            name="date",
            field=models.DateTimeField(
                blank=True, default=django.utils.timezone.now, editable=False
            ),
        ),
    ]
