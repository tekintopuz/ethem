from django.views.generic import RedirectView
from django.views.static import serve
from django.contrib import admin
from django.urls import path, include, re_path
from user.urls import urlpatterns as user_urlpatterns
from citizen.urls import urlpatterns as citizen_urlpatterns
from mysite import settings

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^favicon", RedirectView.as_view(url='/media/logo.png', permanent=True), name="favicon_view"),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT,
                                              'show_indexes': settings.DEBUG}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,
                                             'show_indexes': settings.DEBUG}),
    path('', include('user.urls')),
]

urlpatterns += user_urlpatterns
urlpatterns += citizen_urlpatterns