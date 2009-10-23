from django.http import HttpResponse
from django.template import Context, loader
from calendars.techs.models import Shift, Tech, Type, Facility, Entry
from datetime import datetime, date, time

def icalendartech(request, tech_request):
	allshifts = Entry.objects.filter(tech__tech__startswith = tech_request)
	template = loader.get_template('techs/template.ical')
	context = Context({
		'allshifts': allshifts,
	})
	return HttpResponse(template.render(context), mimetype='text/calendar')

def icalendartechs(request):
	allshifts = Entry.objects.all()
	template = loader.get_template('techs/template.ical')
	context = Context({
		'allshifts': allshifts,
	})
	return HttpResponse(template.render(context), mimetype='text/calendar')

