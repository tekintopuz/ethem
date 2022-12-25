from django.db import models
from django.utils.translation import gettext_lazy as _

from city.models import City
from citizen.models import Citizen
from user.models import User


class CarBrand(models.Model):
    class Meta:
        verbose_name_plural = _('Car Brands')
        verbose_name = _('Car Brand')
        db_table = "car_brand"
        ordering = ["pk"]

    name = models.CharField(max_length=255, blank=True, null=True, unique=True)

    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="carbrand_created_by")
    deleted_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="carbrand_deleted_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)



class CarModel(models.Model):
    class Meta:
        verbose_name_plural = _('Car Models')
        verbose_name = _('Car Mmodel')
        db_table = "car"
        ordering = ["pk"]

    brand = models.ForeignKey(CarBrand, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True, unique=True)

    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="carmodel_created_by")
    deleted_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="carmodel_deleted_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


class Vehicle(models.Model):
    class Meta:
        verbose_name_plural = _('Vehicles')
        verbose_name = _('Vehicle')
        db_table = "vehicle"
        ordering = ["pk"]

    owner = models.ForeignKey(Citizen, blank=True, null=True, on_delete=models.CASCADE)
    model = models.ForeignKey(CarModel, blank=True, null=True, on_delete=models.CASCADE)
    city = models.ForeignKey(City, blank=True, null=True, on_delete=models.CASCADE)
    plate = models.CharField(max_length=255, blank=True, null=True, unique=True)
    chassis_number = models.CharField(max_length=255, blank=True, null=True, unique=True)
    color = models.CharField(max_length=255, blank=True, null=True)

    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="vehicle_created_by")
    deleted_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="vehicle_deleted_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
