# Generated by Django 4.1.1 on 2022-11-12 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("talard", "0003_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="review",
            options={},
        ),
        migrations.AlterField(
            model_name="review",
            name="review_rating",
            field=models.FloatField(),
        ),
    ]
