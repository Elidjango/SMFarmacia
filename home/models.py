#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class login(models.Model):
	username = models.CharField(max_length=25, null=True)
	password = models.CharField(max_length=25, null=True)
	email = models.CharField(max_length=25, null=True)
	first_name = models.CharField(max_length=25, null=True)
	last_name = models.CharField(max_length=25, null=True)

	def __unicode__(self):
		return username