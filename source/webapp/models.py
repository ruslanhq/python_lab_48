from django.db import models


PRODUCT_OTHER_CHOICE = 'Other'
CATEGORY_CHOICES = (
    (PRODUCT_OTHER_CHOICE, 'Other'),
    ('phone', 'Phone'),
    ('pc', "Personal computer"),
    ('camera', 'Camera')
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name of product')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Product description')
    category = models.CharField(max_length=20, null=False, blank=False, default=PRODUCT_OTHER_CHOICE,
                                choices=CATEGORY_CHOICES, verbose_name='Category')
    count = models.IntegerField(verbose_name='Balance')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Price')

    def __str__(self):
        return self.name





