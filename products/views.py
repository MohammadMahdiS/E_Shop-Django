from django.shortcuts import render
from .models import Product, ProductCategory
from django.db.models import Avg

def product_list(request):
    # sample save data in tables
    # playstation = ProductCategory(title='پلی استیشن', url_title='playstation')
    # playstation.save()

    # ps_4 = Product(title='play station 4', price=300, category=playstation, short_description='ps_4_new', rating=4 , is_active=True)
    # ps_4.save()

    products = Product.objects.all()
    number_of_products = products.count()
    avg_rating = products.aggregate(Avg("rating"))
    context = {
        'products': products,
        'total_number_of_products': number_of_products,
        'average_ratings': avg_rating,
    }
    return render(request, 'products/product-list.html', context)

# product detail view with id
def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render(request, 'products/product-detail.html', context)


# product detail view with slug
# def product_detail(request, product_slug):
#     product = Product.objects.get(slug=product_slug)
#     context = {
#         'product': product
#     }
#     return render(request, 'products/product-detail.html', context)
