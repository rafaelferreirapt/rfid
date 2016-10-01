from django.db import models
import uuid


class Hall(models.Model):
    id = models.CharField(max_length=128, default=uuid.uuid4, blank=False, unique=True, primary_key=True)
    tag = models.CharField(max_length=256, blank=False, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ContentHall(models.Model):
    hall = models.ForeignKey('Hall', blank=False)
    url = models.URLField(blank=False)


class HallDistances(models.Model):
    hallA = models.ForeignKey('Hall', blank=False, related_name="hallA")
    hallB = models.ForeignKey('Hall', blank=False, related_name="hallB")
    distance = models.FloatField(blank=False)


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

