from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path , include
from .views import IndexView , CountryView , get_data

urlpatterns = [
    path("" , IndexView.as_view(), name="home"),
    path("country/" ,CountryView.as_view() , name="country_view" ),
    path("api/data/<slug:countryname>" , get_data ,name="api-data"),
]
