from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description_short = models.TextField(
        verbose_name='Краткое описание', blank=True
    )
    description_long = HTMLField(verbose_name='Полное описание', blank=True)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    picture = models.ImageField(verbose_name='Картинка', upload_to='places/')
    place = models.ForeignKey(
        Place, verbose_name='Место картинки',
        related_name='images', on_delete=models.CASCADE
    )
    number_of_image = models.PositiveIntegerField(
        default=0, verbose_name='Номер картинки', blank=True
    )
    
    def __str__(self):
        return f'{self.number_of_image} {self.place}'

    class Meta(object):
        ordering = ['number_of_image']