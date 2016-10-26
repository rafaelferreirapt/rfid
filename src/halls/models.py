from django.db import models
import uuid


class Hall(models.Model):
    id = models.CharField(max_length=128, default=uuid.uuid4, blank=False, unique=True, primary_key=True)
    name = models.CharField(max_length=256, blank=False, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SubHall(models.Model):
    id = models.CharField(max_length=128, default=uuid.uuid4, blank=False, unique=True, primary_key=True)
    name = models.CharField(max_length=256, blank=False, unique=True)

    parent_hall = models.ForeignKey('Hall', blank=False, related_name="parent_hall")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ContentSubHall(models.Model):
    sub_hall = models.ForeignKey('SubHall', blank=False)
    media = models.CharField(max_length=256, blank=False)
    url = models.URLField(blank=False)


class SubHallConnection(models.Model):
    sub_hallA = models.ForeignKey('SubHall', blank=False, related_name="sub_hallA")
    sub_hallB = models.ForeignKey('SubHall', blank=False, related_name="sub_hallB")
    distance = models.FloatField(blank=False)
    connected = models.BooleanField(default=False)


class Category(models.Model):
    id = models.CharField(max_length=128, default=uuid.uuid4, blank=False, unique=True, primary_key=True)
    name = models.CharField(max_length=256, blank=False)
    description = models.CharField(max_length=512, blank=False)

    sub_hall = models.ForeignKey('SubHall', blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SubHallTag(models.Model):
    tag = models.CharField(max_length=256, blank=False, unique=True)
    parent_hall = models.ForeignKey('SubHall', blank=False)


