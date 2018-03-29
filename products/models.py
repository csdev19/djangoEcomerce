from django.db import models
# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.conf import settings

# Create your models here.
class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    slug = models.SlugField()
    categories = models.ManyToManyField('products.ProductCategory')

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def __str__ (self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(
        'products.Product', on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField()

    def __str__ (self):
        return self.image.url



class ProductCategory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__ (self):
        return self.name

class LogBuy(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
    )    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    
    def __str__(self):
        return 'product {} buyed'.format(self.product)

