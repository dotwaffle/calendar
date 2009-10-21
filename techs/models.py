from django.db import models

class Type(models.Model):
	type        = models.CharField(max_length=50)
	def __unicode__(self):
		return self.type

class Shift(models.Model):
	shift       = models.DateTimeField('Shift')
	timestart   = models.TimeField()
	duration    = models.TimeField()
	def __unicode__(self):
		return self.shift

class Tech(models.Model):
	tech        = models.CharField(max_length=50)
	def __unicode__(self):
		return self.tech

class Entry(models.Model):
	uid         = models.AutoField(primary_key=True)
	shift       = models.ManyToManyField(Shift)
	datestamp   = models.DateTimeField(auto_now=True, 'Date Modified')
	datestart   = models.DateField('Date Shift Starts')
	count       = models.IntegerField()
	tech        = models.ManyToManyField(Tech)
	type        = models.ManyToManyField(Type)
	def __unicode__(self):
		return self.datestart


