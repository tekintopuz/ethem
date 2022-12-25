from django.db import models
from django.utils.translation import gettext_lazy as _
from user.models import User
from utils.constants import *


class City(models.Model):
    class Meta:
        verbose_name_plural = 'Cities'
        verbose_name = 'City'
        db_table = "city"
        ordering = ["name"]

    name = models.CharField(max_length=250)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="city_created_by")
    deleted_by = models.ForeignKey(User, null=True, verbose_name=_("Created By"), on_delete=models.CASCADE,
                                   related_name="city_deleted_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    raw_id_fields = ("name",)

    def __str__(self):
        return self.name

