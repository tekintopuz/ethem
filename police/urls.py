from django.urls import re_path
from citizen.views import *


urlpatterns = [
    re_path(r'^police-officers/$', AllPoliceOfficersView.as_view(), name="all_citizen_view"),
    re_path(r'^police-officer/(?P<police_officer_id>\d+)/$', CitizenView.as_view(), name="citizenview"),
    re_path(r'^new-citizen/$', CitizenView.as_view(), name="new_citizen_view"),
    re_path(r"^datatable/all-police-officers/$", AlLPoliceOfficersDatatableView.as_view(), name="datatable_all_users"),
]