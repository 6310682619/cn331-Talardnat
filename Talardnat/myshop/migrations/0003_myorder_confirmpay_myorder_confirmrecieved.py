# Generated by Django 4.1.1 on 2022-11-19 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myshop", "0002_delete_review"),
    ]

    operations = [
        migrations.AddField(
            model_name="myorder",
            name="confirmpay",
            field=models.CharField(default="not pay yet.", max_length=64),
        ),
        migrations.AddField(
            model_name="myorder",
            name="confirmrecieved",
            field=models.CharField(default="not recieve yet.", max_length=64),
        ),
    ]
