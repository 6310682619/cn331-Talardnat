# Generated by Django 4.1.3 on 2022-11-05 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("myshop", "0002_alter_shop_detail_interact_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="shop",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="prod",
                to="myshop.shop_detail",
            ),
        ),
    ]
