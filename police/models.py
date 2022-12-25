from django.db import models
from django.utils.translation import gettext_lazy as _

from citizen.models import Citizen
from city.models import City
from user.models import User


class PoliceDepartment(models.Model):
    class Meta:
        verbose_name_plural = _('Police Departments')
        verbose_name = _('Police Department')
        db_table = "police_department"
        ordering = ["pk"]

    name = models.CharField(max_length=255, blank=True, null=True)

    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="policedepartment_created_by")
    deleted_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="policedepartment_deleted_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.pk}. {self.name}"

class PoliceStation(models.Model):
    class Meta:
        verbose_name_plural = _('Police Stations')
        verbose_name = _('Police Station')
        db_table = "police_station"
        ordering = ["pk"]

    city = models.ForeignKey(City, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    departments = models.ManyToManyField(PoliceDepartment)

    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="policestation_created_by")
    deleted_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="policestation_deleted_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.pk}. {self.name}"


class PoliceOfficer(models.Model):
    class Meta:
        verbose_name_plural = _('Police Officers')
        verbose_name = _('Police Officer')
        db_table = "police_officer"
        ordering = ["pk"]

    citizen = models.ForeignKey(Citizen, blank=True, null=True, on_delete=models.CASCADE)
    department = models.ForeignKey(PoliceDepartment, blank=True, null=True, on_delete=models.CASCADE)
    station = models.ForeignKey(PoliceStation, blank=True, null=True, on_delete=models.CASCADE)
    rank = models.IntegerField(default=1)
    tenure = models.FloatField(default=0.0)

    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="policeofficer_created_by")
    deleted_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="policeofficer_deleted_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.pk}. {self.department.name} - {self.station.name} "
