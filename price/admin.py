from django.contrib import admin

from .models import Card, Service


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('price', 'description')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'old_price', 'new_price')
