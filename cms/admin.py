from django.contrib import admin
from django.utils.safestring import mark_safe

from cms.models import Slider


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'get_image')
    fields = ('title', 'text', 'css', 'img', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" width="128" height="72">')

    get_image.short_description = "Изображение"
