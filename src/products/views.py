# coding=utf-8
from rest_framework import viewsets, mixins
from .models import Product, ProductHalls
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from halls.models import Hall


class ProductsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.filter()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        product = get_object_or_404(Product.objects.all(), id=kwargs.get('pk', ''))
        serializer = self.serializer_class(product)
        return Response(serializer.data)


class ProductsHallsViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.filter()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        hall = get_object_or_404(Hall.objects.all(), id=kwargs.get('pk', ''))
        products = [p.product for p in ProductHalls.objects.filter(hall=hall)]
        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data)

