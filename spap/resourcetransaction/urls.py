from django.conf.urls import url
from . import views

urlpatterns = [

	# All kind of transaction	
    url(r'^seedcoll/$', views.SeedCollectionAPI.as_view() ),
    url(r'^seeddist/$', views.SeedDistributionAPI.as_view() ),

]

