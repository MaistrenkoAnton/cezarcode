from __future__ import unicode_literals
from django.db import models


class Note(models.Model):
    label = models.CharField(max_length=256)
    shifr = models.CharField(max_length=256)
    ROT = models.IntegerField()
