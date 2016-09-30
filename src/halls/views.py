# coding=utf-8
from rest_framework import viewsets, mixins
from .models import Hall, ContentHall
from .serializers import HallSerializer, ContentHallSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class HallsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Hall.objects.filter()
    serializer_class = HallSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        hall = get_object_or_404(Hall.objects.all(), tag=kwargs.get('pk', ''))
        serializer = self.serializer_class(hall)
        return Response(serializer.data)


class ContentHallViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = ContentHall.objects.filter()
    serializer_class = ContentHallSerializer

    def retrieve(self, request, *args, **kwargs):
        hall = get_object_or_404(Hall.objects.all(), id=kwargs.get('pk', ''))
        urls = [p.url for p in ContentHall.objects.filter(hall=hall)]
        serializer = self.serializer_class(urls, many=True)
        return Response(serializer.data)

