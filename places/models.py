from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description_short = models.TextField(verbose_name="Краткое описание")
    description_long = HTMLField(verbose_name="Полное описание")
    lng = models.FloatField(verbose_name="Долгота")
    lat = models.FloatField(verbose_name="Широта")


    def __str__(self):
        return self.title
