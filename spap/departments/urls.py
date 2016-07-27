from django.conf.urls import url
import views

urlpatterns = [

	# All order details	
    url(r'^dvision/$', views.DivisionAPI.as_view() ),
    url(r'^range/$', views.RangeAPI.as_view() ),
    url(r'^beat/$', views.BeatAPI.as_view() ),

]

