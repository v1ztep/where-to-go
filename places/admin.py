from django.contrib import admin

from .models import Image
from .models import Place

admin.site.register(Place)
admin.site.register(Image)
