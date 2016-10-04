# coding=utf-8
from rest_framework import viewsets, mixins
from halls.models import CategoryHalls, Category
from category.serializers import CategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from halls.models import Hall


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.filter()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        product = get_object_or_404(Category.objects.all(), id=kwargs.get('pk', ''))
        serializer = self.serializer_class(product)
        return Response(serializer.data)


class CategoryHallsViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.filter()
    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        hall = get_object_or_404(Hall.objects.all(), tag=kwargs.get('pk', ''))
        categories = [p.category for p in CategoryHalls.objects.filter(hall=hall)]
        serializer = self.serializer_class(categories, many=True)
        return Response(serializer.data)

