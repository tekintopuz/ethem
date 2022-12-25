from django.db import models
from django.utils.translation import gettext_lazy as _

from citizen.models import Citizen
from user.models import User


class Solicitor(models.Model):
    class Meta:
        verbose_name_plural = _('Solicitors')
        verbose_name = _('Solicitor')
        db_table = "solicitor"
        ordering = ["pk"]

    citizen = models.ForeignKey(Citizen, blank=True, null=True, on_delete=models.CASCADE)
    bar_association = models.CharField(max_length=255, blank=True, null=True)

    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="solicitor_created_by")
    deleted_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="solicitor_deleted_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
