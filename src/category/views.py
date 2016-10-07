# coding=utf-8
from rest_framework import views, viewsets, mixins, status
from halls.models import CategoryHalls, Category
from category.serializers import CategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from halls.models import Hall
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


class CategoryHallsViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.filter()
    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        hall = get_object_or_404(Hall.objects.all(), tag=kwargs.get('pk', ''))
        categories = [p.category for p in CategoryHalls.objects.filter(hall=hall)]
        serializer = self.serializer_class(categories, many=True)
        return Response(serializer.data)


class SearchCategoryDetails(views.APIView):

    @staticmethod
    def get(request, current_tag, category_id):
        category = get_object_or_404(Category.objects.all(), id=category_id)
        hall_to = CategoryHalls.objects.get(category=category).hall
        w = Way()
        response = w.search_path(from_point=current_tag, to=hall_to.tag)
        return Response(response[0], status=status.HTTP_200_OK)
