# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    image = models.TextField(max_length=255, null=True, blank=True)
    customer_id = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Weight(models.Model):

    #__Weight_FIELDS__
    id_user = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    date = models.TextField(max_length=255, null=True, blank=True)
    time = models.TextField(max_length=255, null=True, blank=True)

    #__Weight_FIELDS__END

    class Meta:
        verbose_name        = _("Weight")
        verbose_name_plural = _("Weight")


class Metrics(models.Model):

    #__Metrics_FIELDS__
    birthday = models.TextField(max_length=255, null=True, blank=True)
    gender = models.TextField(max_length=255, null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    goal = models.TextField(max_length=255, null=True, blank=True)
    activitylevel = models.IntegerField(null=True, blank=True)
    caloriesadjustment = models.IntegerField(null=True, blank=True)
    proteindistribution = models.IntegerField(null=True, blank=True)
    fatdistribution = models.IntegerField(null=True, blank=True)
    carbsdistribution = models.IntegerField(null=True, blank=True)
    id_user = models.IntegerField(null=True, blank=True)

    #__Metrics_FIELDS__END

    class Meta:
        verbose_name        = _("Metrics")
        verbose_name_plural = _("Metrics")



#__MODELS__END
