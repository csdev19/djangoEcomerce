from django.db import models

# Create your models here.
class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    slug = models.SlugField()

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

