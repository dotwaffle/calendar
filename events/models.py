from django.db import models

class Area(models.Model):
	area        = models.CharField(max_length=200)
	def __unicode__(self):
		return self.area

class Site(models.Model):
	site        = models.CharField(max_length=200)
	def __unicode__(self):
		return self.site

class Severity(models.Model):
	severity    = models.CharField(max_length=200)
	def __unicode__(self):
		return self.severity

class Entry(models.Model):
	uid         = models.AutoField(primary_key=True)
	area        = models.ManyToManyField(Area)
	site        = models.ManyToManyField(Site)
	datestamp   = models.DateTimeField('Date Modified', auto_now=True)
	datestart   = models.DateTimeField('Date Started')
	datefinish  = models.DateTimeField('Date Finished')
	summary     = models.CharField(max_length=200)
	severity    = models.ManyToManyField(Severity)
	description = models.TextField()
	def __unicode__(self):
		return self.summary


