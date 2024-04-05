from django.db import models

from products.models import Product


class ProductAdditionalInformation(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='additional_information')
    additional_information = models.TextField()
