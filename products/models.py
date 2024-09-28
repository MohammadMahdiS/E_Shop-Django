from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.urls import reverse


class ProductCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    url_title = models.CharField(max_length=255, verbose_name="عنوان در url")

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)
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