from django.http import HttpResponse
from django.template import Context, loader
from calendars.events.models import Entry, Area, Site, Severity
from datetime import datetime, date, time

def icalendararea(request, area_request):
	allevents = Entry.objects.filter(area__area__startswith = area_request)
#	for i in allevents:
#		i = i.replace(\n, "\n")
	template = loader.get_template('events/template.ical')
	context = Context({
		'allevents': allevents,
	})
	return HttpResponse(template.render(context), mimetype='text/calendar')

def icalendarsite(request, site_request):
	allevents = Entry.objects.filter(site__site__startswith = site_request)
#	for i in allevents:
#		i = i.replace(\n, "\n")
	template = loader.get_template('events/template.ical')
	context = Context({
		'allevents': allevents,
	})
	return HttpResponse(template.render(context), mimetype='text/calendar')

def icalendar(request):
	allevents = Entry.objects.all()
#	for event in allevents:
#		event.description = event.description.replace(\n, "\n")
	template = loader.get_template('events/template.ical')
	context = Context({
		'allevents': allevents,
	})
	return HttpResponse(template.render(context), mimetype='text/calendar')

