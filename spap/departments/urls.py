from django.conf.urls import url
from . import views

urlpatterns = [

    # All order details 
    url(r'^division/$', views.DivisionAPI.as_view() ),
    url(r'^range/$', views.RangeAPI.as_view() ),
    url(r'^beat/$', views.BeatAPI.as_view() ),

]

