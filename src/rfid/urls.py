from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

from halls.urls import router as halls_urls
from category.urls import router as category_urls

urlpatterns = [
               url(r'^admin/', include(admin.site.urls)),
               url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

               # pages
               url(r'^api/v1/category/', include(category_urls.urls)),
               url(r'^api/v1/halls/', include(halls_urls.urls)),

               url('^.*$', TemplateView.as_view(template_name='index.html'), name='index')
               ]
