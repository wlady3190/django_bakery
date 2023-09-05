from django.db import models
from django.utils.timezone import now

# Create your models here.


class Category(models.Model):
    categoryName = models.CharField(max_length=100)

    class Meta:
        ordering = ['categoryName',]

    def __str__(self):
        return self.categoryName


class Product(models.Model):
    productName = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    image = models.ImageField(upload_to='products', default='pastel_default.png')
    createdProduct = models.DateTimeField(default=now)
    modifiedProduct = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ['productName']

    def __str__(self):
        return self.productName
