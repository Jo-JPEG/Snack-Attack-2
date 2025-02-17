# Generated by Django 5.0.1 on 2025-02-17 11:03

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("snake", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="image",
            field=cloudinary.models.CloudinaryField(
                default="placeholder", max_length=255, verbose_name="image"
            ),
        ),
    ]
