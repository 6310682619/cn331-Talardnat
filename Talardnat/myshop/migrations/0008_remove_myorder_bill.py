# Generated by Django 4.1.1 on 2022-11-12 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myshop", "0007_remove_myorder_prod_myorder_prod"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="myorder",
            name="bill",
        ),
    ]
