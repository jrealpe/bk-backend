from django.contrib import admin

from .models import *


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'province')
    search_fields = ('name', 'province__name')


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'iso_3166_2')
