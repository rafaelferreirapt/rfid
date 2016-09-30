from django.db import models
import uuid
from halls.models import Hall


class Product(models.Model):
    id = models.CharField(max_length=128, default=uuid.uuid4, blank=False, unique=True, primary_key=True)
    name = models.CharField(max_length=256, blank=False)
    description = models.CharField(max_length=512, blank=False)
    brand = models.CharField(max_length=256, blank=False)
    price = models.FloatField(blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductHalls(models.Model):
    product = models.ForeignKey('Product', blank=False)
    hall = models.ForeignKey('Hall', blank=False)

