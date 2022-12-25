from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import User
from django.utils.translation import gettext_lazy as _


class UserAdminConfig(UserAdmin):
    # ordering, list_display, etc..
    search_fields = ('id', 'first_name', 'last_name', 'email')
    model = User
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"), {
                "fields": (
                    "avatar",
                    "first_name",
                    "last_name",
                    "email",
                    "phone",
                    "deleted_by")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "secret",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_deleted",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            _("Important dates"),
            {
                "fields": (
                    "deleted_at",
                    "last_login",
                    "date_joined"
                )}),
    )
    readonly_fields = ('secret',)


admin.site.register(User, UserAdminConfig)
