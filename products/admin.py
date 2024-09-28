from django.contrib import admin
from .models import Product



class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug']
    prepopulated_fields = {
        'slug': ['title']
    }

    list_display = ['__str__', 'title', 'price', 'short_description', 'rating', 'is_active']
    list_editable = ['title', 'rating', 'price', 'short_description', 'is_active']
    list_filter = ['title', 'price']
    search_fields = ['title', 'price', 'rating']
    
admin.site.register(Product, ProductAdmin)