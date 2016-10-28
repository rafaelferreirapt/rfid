# coding=utf-8
from rest_framework import views, viewsets, mixins, status
from halls.models import Category, SubHallTag
from category.serializers import CategorySerializer
from halls.serializers import SubHallSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from halls.models import SubHall
from way import Way


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


class CategorySubHallsViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.filter()
    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        sub_hall = get_object_or_404(SubHallTag.objects.all(), tag=kwargs.get('pk', '')).parent_hall
        serializer = self.serializer_class(Category.objects.filter(sub_hall=sub_hall), many=True)
        return Response(serializer.data)


class SearchCategoryDetails(views.APIView):

    @staticmethod
    def get(request, current_tag, category_id):
        category = get_object_or_404(Category.objects.all(), id=category_id)
        sub_hall_to = category.sub_hall
        w = Way()
        response = w.search_path(from_point=current_tag, to=sub_hall_to.name)
        halls = []

        for row in response[0]:
            halls += [SubHall.objects.get(name=row)]

        serializer = SubHallSerializer(halls, many=True)
        return Response(serializer.data)
