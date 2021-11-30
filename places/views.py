from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from .models import Place


def index(request):
    places = Place.objects.all()
    details_of_places = []

    for place in places:
        detail_place = {
            'type': 'FeatureCollection',
            'features': [{
                'type': 'Feature',
                'geometry': {
                  'type': 'Point',
                  'coordinates': [place.lng, place.lat]
                },
                'properties': {
                  'title': place.title,
                  'placeId': place.id,
                  'detailsUrl': reverse('place', args=[place.id])
                }
            }]
        }
        details_of_places.append(detail_place)

    context = {'value': details_of_places}
    return render(request, 'index.html', context=context)


def post(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_details = {
        'title': place.title,
        'imgs': [image.picture.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lat,
            'lng': place.lng
        }
    }
    response = JsonResponse(
        place_details, safe=False,
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 4
        }
    )
    return response
