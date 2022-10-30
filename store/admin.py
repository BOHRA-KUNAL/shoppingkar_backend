from django.contrib import admin
from . import models


@admin.register(models.Product)

class ProductAdmin(admin.ModelAdmin):
    list_display= ['title', 'price']
    prepopulated_fields = {
        'slug': ['title']
    }


@admin.register(models.Collection)

class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {
        'slug': ['title']
    }

