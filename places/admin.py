from django.contrib import admin

from .models import Image
from .models import Place


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

class ImageInline(admin.TabularInline):
    model = Image

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]
