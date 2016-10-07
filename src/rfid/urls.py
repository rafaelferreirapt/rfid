from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

from halls.urls import router as halls_urls
from category.urls import router as category_urls
from category.views import SearchCategoryDetails


urlpatterns = [
               url(r'^admin/', include(admin.site.urls)),
               url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

               # pages
               url(r'^api/v1/category/', include(category_urls.urls)),
               url(r'^api/v1/halls/', include(halls_urls.urls)),
               url(r'^api/v1/category/search/(?P<current_tag>.+)/(?P<category_id>.+)/$',
                   SearchCategoryDetails.as_view(), name="Category search"),

               url('^.*$', TemplateView.as_view(template_name='index.html'), name='index')
               ]
