from __future__ import unicode_literals

from django.db import models


# Create your models here.
class TwitterProfile(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=500, null=True)