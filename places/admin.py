from adminsortable2.admin import SortableAdminMixin
from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Image
from .models import Place


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    raw_id_fields = ["place"]

class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ['preview_image']
    fields = ["picture", "place", "preview_image", "number_of_image"]
    extra = 1

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
    search_fields = ['title']
    inlines = [
        ImageInline
    ]
