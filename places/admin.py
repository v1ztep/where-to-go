from django.contrib import admin
from django.utils.html import format_html

from .models import Image
from .models import Place


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['preview_image']
    fields = ["picture", "place", "preview_image", "number_of_image"]

    def preview_image(self, obj):
        return format_html(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.picture.url,
                width='auto',
                height='200px',
            )
        )

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]
