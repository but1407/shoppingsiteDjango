# Generated by Django 4.2.11 on 2024-03-14 04:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="product_img",
            field=models.CharField(default="", max_length=255),
        ),
    ]
