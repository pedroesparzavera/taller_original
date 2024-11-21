# Generated by Django 5.1 on 2024-11-17 03:23

import base_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0004_seeding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=base_app.models.get_file_path),
        ),
    ]
