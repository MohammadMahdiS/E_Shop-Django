from django.urls import path
from .views import product_list, product_detail
urlpatterns = [
    path('list/', product_list, name="product-list-page"),
    # product detail with id
    path('<int:product_id>/', product_detail, name="product-detail-page"),
    # product detail with slug
    # path('<slug:product_slug>/', product_detail, name="product-detail-page"),
    
]