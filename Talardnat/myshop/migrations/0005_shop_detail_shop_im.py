# Generated by Django 4.1.1 on 2022-11-19 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myshop", "0004_myorder_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="shop_detail",
            name="shop_im",
            field=models.ImageField(
                default="https://webstockreview.net/images/mcdonalds-clipart-storefront-1.png",
                upload_to="images/",
            ),
        ),
    ]