from django.shortcuts import render
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
                  'detailsUrl': '../static/places/moscow_legends.json'
                }
            }]
        }
        details_of_places.append(detail_place)

    context = {'value': details_of_places}
    return render(request, 'index.html', context=context)
