from django.contrib import admin
from .models import Product, ProductCategory, ProductInformation



class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug']
    prepopulated_fields = {
        'slug': ['title']
    }

    list_display = ['__str__', 'title', 'price', 'short_description', 'rating', 'is_active', 'category']
    list_editable = ['title', 'rating', 'price', 'short_description', 'is_active']
    list_filter = ['title', 'price']
    search_fields = ['title', 'price', 'rating']

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__','title', 'url_title']
    list_editable = ['title', 'url_title']
    list_filter = ['title', 'url_title']
    search_fields = ['title', 'url_title']

class ProductInformationAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'color', 'size']
    list_editable = ['color', 'size']
    list_filter = ['color', 'size']
    search_fields = ['color', 'size']

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductInformation, ProductInformationAdmin )