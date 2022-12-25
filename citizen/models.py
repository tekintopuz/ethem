from django.db import models
from django.utils.translation import gettext_lazy as _

from user.models import User
from utils.constants import MALE, FEMALE


class FingerPrint(models.Model):
    class Meta:
        verbose_name_plural = _('Finger Prints')
        verbose_name = _('Finger Print')
        db_table = "finger_print"
        ordering = ["pk"]

    detail = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="fingerprint_created_by")
    deleted_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="fingerprint_deleted_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


class DNARecord(models.Model):
    class Meta:
        verbose_name_plural = _('DNA Records')
        verbose_name = _('DNA Record')
        db_table = "dna_record"
        ordering = ["pk"]

    detail = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="dna_record_created_by")
    deleted_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="dna_record_deleted_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


class FamilyTree(models.Model):
    class Meta:
        verbose_name_plural = _('Family Trees')
        verbose_name = _('Family Tree')
        db_table = "family_tree"
        ordering = ["pk"]

    name = models.CharField(max_length=255, blank=True, null=True)

    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="familytree_created_by")
    deleted_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="familytree_deleted_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


class Citizen(models.Model):
    class Meta:
        verbose_name_plural = _('Citizens')
        verbose_name = _('Citizen')
        db_table = "citizen"
        ordering = ["pk"]

    GENDER = ((MALE, "male"),
              (FEMALE, "female"))

    mother = models.ForeignKey("Citizen", blank=True, null=True, on_delete=models.CASCADE, related_name="citizen_mother")
    father = models.ForeignKey("Citizen", blank=True, null=True, on_delete=models.CASCADE, related_name="citizen_father")
    family_tree = models.ForeignKey(FamilyTree, blank=True, null=True, on_delete=models.CASCADE)
    dna_record = models.ForeignKey(DNARecord, blank=True, null=True, on_delete=models.CASCADE)
    finger_print = models.ForeignKey(FingerPrint, blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True, choices=GENDER)
    email = models.CharField(max_length=255, blank=True, null=True, unique=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    birth_place = models.CharField(max_length=255, blank=True, null=True)

    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="citizen_created_by")
    deleted_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="citizen_deleted_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
