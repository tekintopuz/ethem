from django.urls import re_path
from citizen.views import *


urlpatterns = [
    re_path(r'^citizens/$', AllCitizensView.as_view(), name="all_citizen_view"),
    re_path(r'^citizen/(?P<citizen_id>\d+)/$', CitizenView.as_view(), name="citizenview"),
    re_path(r'^new-citizen/$', CitizenView.as_view(), name="new_citizen_view"),
    re_path(r"^datatable/all-citizens/$", AlLCitizensDatatableView.as_view(), name="datatable_all_users"),
]