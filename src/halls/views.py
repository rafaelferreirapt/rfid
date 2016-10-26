# coding=utf-8
from rest_framework import viewsets, mixins
from halls.models import Hall, SubHall, ContentSubHall, SubHallTag
from halls.serializers import HallSerializer, SubHallSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class HallsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Hall.objects.filter()
    serializer_class = HallSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        hall = get_object_or_404(Hall.objects.all(), name=kwargs.get('pk', ''))
        serializer = self.serializer_class(hall)
        return Response(serializer.data)


class SubHallsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = SubHall.objects.filter()
    serializer_class = SubHallSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        hall = get_object_or_404(SubHall.objects.all(), name=kwargs.get('pk', ''))
        serializer = self.serializer_class(hall)
        return Response(serializer.data)


class ContentSubHallViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = ContentSubHall.objects.filter()
    serializer_class = HallSerializer

    def retrieve(self, request, *args, **kwargs):
        sub_hall = get_object_or_404(SubHallTag.objects.all(), tag=kwargs.get('pk', '')).parent_hall

        contents = []

        for p in ContentSubHall.objects.filter(sub_hall=sub_hall):
            entry = {
                "media": str(p.media),
                "url": str(p.url)
            }
            contents.append(entry)

        return Response(contents)

