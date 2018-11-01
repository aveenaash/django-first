# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class Customer(models.Model):
	firstName  = models.CharField(max_length = 50)
	lastName = models.CharField(max_length = 50)
	dob = models.DateField()
	createdAt = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return self.firstName + " " + self.lastName