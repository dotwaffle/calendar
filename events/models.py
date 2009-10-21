from django.db import models

class Entry(models.Model):
	uid         = models.AutoField(primary_key=True)
	datestamp   = models.DateTimeField('Date Modified')
	datestart   = models.DateTimeField('Date Started')
	datefinish  = models.DateTimeField('Date Finished')
	summary     = models.CharField(max_length=200)
	description = models.TextField()
	def __unicode__(self):
		return self.summary

