# Generated by Django 3.2.9 on 2021-12-07 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20211203_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='number_of_image',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Номер картинки'),
        ),
    ]