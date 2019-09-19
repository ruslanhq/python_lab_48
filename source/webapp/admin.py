from django.contrib import admin
from webapp.models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'description', 'category', 'count', 'price']
    list_filter = ['category', 'price']
    list_display_links = ['pk', 'name']
    search_fields = ['name', 'category']
    fields = ['name', 'description', 'category', 'count', 'price']


admin.site.register(Product, ProductAdmin)



