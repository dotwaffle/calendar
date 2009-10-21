from django.http import HttpResponse
from django.template import Context, loader
from calendars.events.models import Entry, Area
from datetime import datetime, date, time

def icalendar(request, area_request):
	allevents = Entry.objects.filter(area__area__startswith = area_request)
	template = loader.get_template('events/template.ical')
	context = Context({
		'allevents': allevents,
	})
	return HttpResponse(template.render(context), mimetype='text/calendar')

