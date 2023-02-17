from django.db import models


# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, blank=True, null=True)
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField()
    color = models.CharField(max_length=50)
    memory = models.IntegerField()
    image = models.ImageField(upload_to='products_images')
    sim = models.BooleanField(default=True)
    esim = models.BooleanField(default=False)
    origin_country = models.CharField(max_length=50)
    materials = models.TextField(blank=True, null=True)
    os = models.CharField(max_length=20)
    vendor_code = models.IntegerField()
    guarantee = models.IntegerField()
    nfc = models.BooleanField(default=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return f'{self.name}'
