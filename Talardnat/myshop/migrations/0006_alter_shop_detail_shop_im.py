# Generated by Django 4.1.1 on 2022-11-19 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myshop", "0005_shop_detail_shop_im"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shop_detail",
            name="shop_im",
            field=models.ImageField(
                default="/images/cartoon-style-cafe-front-shop-view_134830-697.webp",
                upload_to="images/",
            ),
        ),
    ]
