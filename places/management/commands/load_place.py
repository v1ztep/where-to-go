from pathlib import Path
from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Image
from places.models import Place


class Command(BaseCommand):
    help = 'Upload place from Json'

    def add_arguments(self, parser):
        parser.add_argument('urls', nargs='+', type=str)

    def handle(self, *args, **options):
        for url in options.get('urls'):
            response = requests.get(url, allow_redirects=False)
            response.raise_for_status()
            detail_place = response.json()

            place, _ = Place.objects.get_or_create(
                title = detail_place['title'],
                defaults = {
                    'description_short': detail_place['description_short'],
                    'description_long': detail_place['description_long'],
                    'lng': detail_place['coordinates']['lng'],
                    'lat': detail_place['coordinates']['lat']
                }
            )

            for image_numb, image_url in enumerate(detail_place['imgs'], start=1):
                response = requests.get(image_url, allow_redirects=False)
                response.raise_for_status()
                content = ContentFile(response.content)
                image_name = Path(urlparse(image_url).path).name
                new_image = Image(place=place, number_of_image=image_numb)
                new_image.picture.save(image_name, content, save=True)
