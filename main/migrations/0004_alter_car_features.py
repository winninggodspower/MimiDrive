# Generated by Django 5.0.3 on 2024-03-06 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_car_main_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='features',
            field=models.ManyToManyField(blank=True, null=True, to='main.feature'),
        ),
    ]
