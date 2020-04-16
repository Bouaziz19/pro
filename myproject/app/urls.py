
from django.urls import path
from django.http import HttpResponse
from django.conf.urls import url
from . import views
urlpatterns = [
    path('AG/', views.page_ac, name='index'),
    path('AG/change/', views.page2_ac, name='index'),
    path('AG/get_res_page/', views.get_res_page, name='index4'),
    path('AG/save_page/', views.save_page,name='save_page'),
    path('AG/stop_pros/', views.stop_pros,name='stop_pros'),
    path('AG/str_ag/', views.str_ag, name='index2'),]
    