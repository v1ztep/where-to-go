# Generated by Django 3.2.9 on 2021-12-03 18:44

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_place_description_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True, verbose_name='Краткое описание'),
        ),
    ]