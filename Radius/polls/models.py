from django.db import models

# Create your models here.


class Question(models.Model):
    CATEGORY_CHOICES = (
        ('Ethernet Router', 'Ethernet Router'),
        ('switch', 'switch'),
        ('Wireless System', 'Wireless System'),
        ('Wireless For Home and Office', 'Wireless For Home and Office'),
        ('LTE Product', 'LTE Product'),
        ('interface', 'interface'),
        ('Accessories', 'Accessories'),
    )
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='product_image', blank=True)
    product = models.CharField(max_length=200, verbose_name="ürün")
    Qty = models.IntegerField(default=0, verbose_name="Adet")
    date_of_purchase = models.DateTimeField('Alış tarihi')
    purchase_price = models.DecimalField(decimal_places=2, max_digits=6, verbose_name="Alış ücreti", default=0.0)
    sale_price = models.DecimalField(decimal_places=2, max_digits=6, verbose_name="Satış ücreti", default=0.0)
    comment = models.TextField(blank=True, verbose_name="Açıklama")

    def __str__(self):
        return self.product


class Sold_Product(models.Model):
    sold_product = models.CharField(max_length=200, verbose_name="Satılan Ürün")