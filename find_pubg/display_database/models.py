# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	user_id = models.CharField(max_length=20)
	steam_id = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	email = models.CharField(max_length=40)
	has_profile = models.BooleanField(default=False)
	
