from django.db import models
from django.utils.translation import gettext_lazy as _

from car.models import Vehicle
from citizen.models import Citizen
from city.models import City
from police.models import PoliceOfficer
from solicitor.models import Solicitor
from user.models import User
from utils.constants import *


class TrafficPenalty(models.Model):
    class Meta:
        verbose_name_plural = _('Traffic Penalties')
        verbose_name = _('Traffic Penalty')
        db_table = "traffic_penalty"
        ordering = ["pk"]

    vehicle = models.ForeignKey(Vehicle, blank=True, null=True, on_delete=models.CASCADE)
    reporter = models.ForeignKey(PoliceOfficer, blank=True, null=True, on_delete=models.CASCADE)
    offender = models.ForeignKey(Citizen, blank=True, null=True, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places = 2)
    relevant_article = models.CharField(max_length=255, blank=True, null=True)


    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="trafficpenalty_created_by")
    deleted_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="trafficpenalty_deleted_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.pk}. {self.relevant_article}"



class CriminalRecord(models.Model):
    class Meta:
        verbose_name_plural = _('Criminal Records')
        verbose_name = _('Criminal Record')
        db_table = "criminal_record"
        ordering = ["pk"]

    TYPES = ((TRAFFIC_RULES_VIOLATION, "traffic role violation"),
             (BURGLARY, "burglary"),
             (FORGERY, "forgery"),
             (HIJACKING, "hijacking"),
             (MUGGLING, "mugging"),
             (CAR_THEFT, "car theft"),
             )
    city = models.ForeignKey(City, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True, choices=TYPES)
    address = models.CharField(max_length=500, blank=True, null=True)

    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="criminalrecord_created_by")
    deleted_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="criminalrecord_deleted_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.pk}. {self.name}"


class Offender(models.Model):
    class Meta:
        verbose_name_plural = _('Offenders')
        verbose_name = _('Offender')
        db_table = "offender"
        ordering = ["pk"]


    citizen = models.ForeignKey(Citizen, blank=True, null=True, on_delete=models.CASCADE)
    criminal_record = models.ForeignKey(CriminalRecord, blank=True, null=True, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="offender_created_by")
    deleted_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="offender_deleted_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.pk}. {self.citizen.first_name}"



class Victim(models.Model):
    class Meta:
        verbose_name_plural = _('Victims')
        verbose_name = _('Victim')
        db_table = "victim"
        ordering = ["pk"]


    citizen = models.ForeignKey(Citizen, blank=True, null=True, on_delete=models.CASCADE)
    criminal_record = models.ForeignKey(CriminalRecord, blank=True, null=True, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="victim_created_by")
    deleted_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="victim_deleted_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.pk}. {self.citizen.first_name}"


class CriminalRecordSolicitor(models.Model):
    class Meta:
        verbose_name_plural = _('Criminal Record Solicitors')
        verbose_name = _('Criminal Record Solicitor')
        db_table = "criminal_record_solicitor"
        ordering = ["pk"]

    TYPES = ((DEFENSE_ATTORNEY, "defense attorney"),
             (VICTIM_ATTORNEY, "victim's attorney"),
             (ATTORNEY_INVEOLVED, "attorney involved"),

             )

    criminal_record = models.ForeignKey(CriminalRecord, blank=True, null=True, on_delete=models.CASCADE)
    solicitor = models.ForeignKey(Solicitor, blank=True, null=True, on_delete=models.CASCADE)

    started_at = models.DateTimeField(blank=True, null=True)
    end_at = models.DateTimeField(blank=True, null=True)

    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="criminalrecordsolicitor_created_by")
    deleted_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="criminalrecordsolicitor_deleted_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


class CriminalReporter(models.Model):

    class Meta:
        verbose_name_plural = _('Criminal Reporters')
        verbose_name = _('Criminal Reporter')
        db_table = "criminal_recoporter"
        ordering = ["pk"]

    criminal_record = models.ForeignKey(CriminalRecord, blank=True, null=True, on_delete=models.CASCADE)
    officer = models.ForeignKey(PoliceOfficer, blank=True, null=True, on_delete=models.CASCADE)

    started_at = models.DateTimeField(blank=True, null=True)
    end_at = models.DateTimeField(blank=True, null=True)

    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="criminalreporter_created_by")
    deleted_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="criminalreporter_deleted_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)