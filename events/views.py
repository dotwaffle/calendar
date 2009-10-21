from django.http import HttpResponse
from django.template import Context, loader
from maintenance.events.models import Entry
from datetime import datetime, date, time


def index(request):
	allevents = Entry.objects.all()
	template = loader.get_template('events/network.ical')
	context = Context({
		'allevents': allevents,
	})
	return HttpResponse(template.render(context), mimetype='text/calendar')

