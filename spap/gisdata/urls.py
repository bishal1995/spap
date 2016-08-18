from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^gisarea/$', views.gisAreaAPI.as_view() ),
    url(r'^cordinates/$', views.cordinatesAPI.as_view() ),

]

