from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.urls import reverse


class ProductCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    url_title = models.CharField(max_length=255, verbose_name="عنوان در url")

    def __str__(self):
        return f"{self.title}- {self.url_title}"
    
    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی های محصول'

class ProductInformation(models.Model):
    color = models.CharField(max_length=255, verbose_name='رنگ')
    size = models.CharField(max_length=255, verbose_name='سایز')

    def __str__(self):
        return f"{self.color}, {self.size}"
    
    class Meta:
        verbose_name = 'اطلاعات تکمیلی محصول'
        verbose_name_plural = 'تمامی اطلاعات تکمیلی'
    
# in DDB when we have many tables, the relation field must be in main model that other models depeneded on it
class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, related_name="products", verbose_name='دسته بندی')
    information = models.OneToOneField(
        'ProductInformation',
         on_delete=models.CASCADE,
         related_name='product_information',
         verbose_name='اطلاعات تکمیلی',
         null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], default=0
    )
    short_description = models.CharField(max_length=255)
    is_active = models.BooleanField()
    # add slug if use slug for see product detail view with urls slug
    slug = models.SlugField(default="", null=False, db_index=True)

    # use something similar to the url template tag with reverse
    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    # add slug if use slug for see product detail view with urls slug
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"
    
    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'



# shell: save data and select many-to-one relationship
# from products.models import Product, ProductCategory
# mobile = ProductCategory(title='mobile', url_title='mobile')
# mobile.save()
# apple = Product(title='iphone11', category= mobile, price=100, rating=3, short_description = 'ex-max-pro', is_active=True)
# apple.save()

# shell: select in relationship
# iphone = Product.objects.all()[0]
# iphone.category.title         --->  get in Product.category.title ::: mobile
# iphone.category.url_title 


# retrive one product based on its category
# product_by_category = Product.objects.filter(category__url_title='mobile')
# product_by_category2 = Product.objects.filter(category__title='playstation')
# product_by_category3 = Product.objects.filter(category__url_title__contains='p')  
# product_by_category4 = Product.objects.filter(category__title__startswith='پ')

# retrive all list products base on its category, product_set is the all Products in Product table that related with ProductCategory=mobile
# mobile = ProductCategory.objects.get(url_title='mobile')
# mobile.product_set.all()

# retrive all list products base on its category, products(related_name='products') is the all Products in Product table that related with ProductCategory=mobile
# mobile = ProductCategory.objects.get(url_title='mobile')
# mobile.products.all()
# mobile.products.get(title="iphone12")
# mobile.products.filter(title__contains="phone")
