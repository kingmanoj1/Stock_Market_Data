from django.urls import path,include
from . import views

urlpatterns=[
    path("",views.home,name='home'),
    path("google/",views.google,name="google"),
    path("fb/",views.fb,name="fb"),
    path("ibm/",views.ibm,name="ibm"),
    path("sony/",views.sony,name="sony"),
    path("index/",views.index,name="index"),
]