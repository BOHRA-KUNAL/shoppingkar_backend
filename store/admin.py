from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.contrib import admin
from . import models

class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin): 
        return[
            ('<10', 'Low')
        ]
    
    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)

@admin.register(models.Product)

class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    actions = ['clear_inventory']

    list_display= ['title', 'price','Qty', 'inventory_status', 'collection_title']
    prepopulated_fields = {
        'slug': ['title']   
    }
    list_per_page: 10
    list_filter = ['collection', 'last_update', InventoryFilter]
    list_select_related = ['collection']
    search_fields = ['title__istartswith']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')

    def inventory_status(self, product):
        if product.inventory<10:
            return 'Low'
        else:
            return 'High'

    @admin.action(description='Clear Inventory')
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)

        self.message_user(
            request,
            f'{updated_count} products were successfully updated.',
        )


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    list_per_page= 10
    search_fields = ['title__istartswith']
    prepopulated_fields = {
        'slug': ['title']
    }

    def products_count(self, collection):
        return collection.products_count
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )

