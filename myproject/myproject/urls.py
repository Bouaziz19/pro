from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import  include, url
import django.views.static

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),  
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    url(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG})
]


