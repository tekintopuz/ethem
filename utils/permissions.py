from rest_framework import permissions
from utils.constants import CUSTOMER, VENDOR


class PermissionPolicyMixin:

    def check_permissions(self, request):
        try:
            # This line is heavily inspired from `APIView.dispatch`.
            # It returns the method associated with an endpoint.
            handler = getattr(self, request.method.lower())
        except AttributeError:
            handler = None

        if (
                handler
                and self.permission_classes_per_method
                and self.permission_classes_per_method.get(handler.__name__)
        ):
            self.permission_classes = self.permission_classes_per_method.get(handler.__name__)

        super().check_permissions(request)


class IsSuperuser(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False

        if request.user.is_superuser:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return False

        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.author == request.user:
            return True

        if request.user.is_staff and request.method not in self.edit_methods:
            return True

        return False


class IsCustomer(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.role == CUSTOMER:
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.author == request.user:
            return True

        return False


class IsStaff(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return False


class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        from product.models import Product
        if (obj.__class__.__name__ == "User" and obj.user == request.user) or \
                (hasattr(obj, 'created_by') and obj.created_by == request.user) or \
                (hasattr(obj, 'owner') and obj.owner == request.user) or \
                (hasattr(obj, 'vendor') and request.user.role == VENDOR and obj.vendor == request.user.vendor) or \
                (type(obj) is Product and obj.vendor and obj.vendor.user == request.user):
            return True
        return False


class IsVendor(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and (
                request.user.groups.filter(name="Vendor").exists()
                and request.user.role == VENDOR and request.user.vendor):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if (hasattr(obj, 'created_by') and obj.created_by == request.user) or \
                (hasattr(obj, 'owner') and obj.owner == request.user) or \
                (hasattr(obj, 'vendor') and obj.vendor.user == request.user):
            return True
        return False


class IsSuperUserOrVendor(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False

        if request.user.is_superuser or request.user.role == VENDOR:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return False

        if request.user.is_superuser or (obj.__class__.__name__ == "Vendor" and obj.user == request.user) or \
                (hasattr(obj, "vendor") and request.user.role == VENDOR and obj.vendor == request.user.vendor):
            return True

        return False


class IsSuperUserOrOwner(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        from product.models import Product
        if request.user.is_anonymous:
            return False

        if request.user.is_superuser or (obj.__class__.__name__ == "User" and obj.user == request.user) or \
                (hasattr(obj, 'created_by') and obj.created_by == request.user) or \
                (hasattr(obj, 'owner') and obj.owner == request.user) or \
                (hasattr(obj, 'vendor') and obj.vendor == request.user.vendor) or \
                (type(obj) is Product and obj.vendor and obj.vendor.user == request.user):
            return True

        return False
