# Generated by Django 4.1.3 on 2022-11-05 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("seller", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="shop_detail",
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
                ("name", models.CharField(max_length=64)),
                ("category", models.CharField(max_length=10, null=True)),
                ("in_interact", models.CharField(max_length=100, null=True)),
                ("ex_interact", models.CharField(max_length=64, null=True)),
                ("expire", models.IntegerField(default=0)),
                ("queue", models.IntegerField(null=True)),
                (
                    "seller_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="shop",
                        to="seller.seller_detail",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="product",
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
                ("product_name", models.CharField(max_length=64)),
                ("price", models.IntegerField(null=True)),
                ("product_im", models.ImageField(upload_to="images/")),
                (
                    "shop",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prod",
                        to="myshop.shop_detail",
                    ),
                ),
            ],
        ),
    ]
