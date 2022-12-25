from django.urls import re_path
from address.views import *


urlpatterns = [
    re_path(r'^country/?$', CountryView.as_view(), name="country_view"),
    re_path(r'^city/?$', CityView.as_view(), name="city_view"),
    re_path(r'^datatable/country', CountryDatatableView.as_view(), name="country_datatable"),
    re_path(r'^datatable/city', CityDatatableView.as_view(), name="country_datatable")
]
