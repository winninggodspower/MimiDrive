# Generated by Django 5.0.3 on 2024-03-06 14:09

import main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.car_images_path),
        ),
        migrations.AlterField(
            model_name='car',
            name='back_image',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.car_images_path),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine_bay_image',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.car_images_path),
        ),
        migrations.AlterField(
            model_name='car',
            name='front_image',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.car_images_path),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(choices=[('Gasoline', 'Gasoline'), ('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid'), ('Other', 'Other')], max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='interior_image',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.car_images_path),
        ),
        migrations.AlterField(
            model_name='car',
            name='side_image',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.car_images_path),
        ),
        migrations.AlterField(
            model_name='car',
            name='trunk_image',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.car_images_path),
        ),
    ]
