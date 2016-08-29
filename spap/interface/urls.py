from django.conf.urls import url,include
from .views import UserFormView,DashboardView,LogOut

urlpatterns = [
    url(r'^$',UserFormView.as_view(),name="login"),
    url(r'^logOut$',LogOut.as_view(),name="logOut"),
    url(r'^dashboard$',DashboardView.as_view(),name="dashboard"),

]