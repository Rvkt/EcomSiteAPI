from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description', 'category__name')
    list_per_page = 20

admin.site.register(Product, ProductAdmin)

