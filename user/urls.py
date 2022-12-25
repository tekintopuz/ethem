from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from user.views import *


urlpatterns = [
    re_path(r'^401', handler401, name="handler401"),
    re_path(r'^403', handler403, name="handler403"),
    re_path(r'^404', handler404, name="handler404"),
    re_path(r'^500', handler500, name="handler500"),
    re_path(r'^501', handler501, name="handler501"),

    re_path(r'^$', HomeView.as_view(), name="home_view"),
    re_path(r'^login/$', csrf_exempt(LoginView.as_view()), name="login"),
    re_path(r'^logout/$', LogoutView.as_view(), name="logout"),
    re_path(r'^delete-object/?$', DeleteObjectView.as_view(), name="delete_object"),
    re_path(r'^register/$', RegisterView.as_view(), name="register"),
    re_path(r'^signup/$', RegisterView.as_view(), name="register"),

    re_path(r'^login$', LoginView.as_view(), name="login"),
    re_path(r'^logout$', LogoutView.as_view(), name="logout"),
    re_path(r'^update-password/(?P<musteri_id>\d+)/$', SetPassword.as_view(), name="set_password"),
    re_path(r'^get-necessary-data/$',  GetNecessaryDataView.as_view(), name="necessary_admin"),

    re_path(r'^profile/$', MyProfileView.as_view(), name="my_profile"),
    re_path(r'^tum-musteriler/$', TumMusterilerView.as_view(), name="tum_musteriler_view"),
    re_path(r'^musteri/(?P<musteri_id>\d+)/$', MusteriView.as_view(), name="client_view"),
    re_path(r'^yeni-musteri/$', MusteriView.as_view(), name="new_client_view"),

    re_path(r'^users/$', AllUsersView.as_view(), name="all_users_view"),
    re_path(r"^datatable/all-users/$", AllUsersDatatableView.as_view(), name="datatable_all_users"),
    re_path(r'^datatable/tum-musteriler/', TumMusterilereDatatableView.as_view(),
            name="tum_musteriler_datatable"),
]