import logging
import datetime

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

from config import codes

class Accumulation(models.Model):
    user_id = models.IntegerField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    status = models.IntegerField(default=codes.StatusCode.AVAILABLE.value, db_index=True)
    production_id = models.CharField(max_length=20)
    production_number = models.IntegerField(default=0)
    coefficient = models.IntegerField(default=0)
    accumulation_number = models.IntegerField(default=0)
    comment = models.CharField(max_length=1024)

