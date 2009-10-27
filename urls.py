from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^calendars/', include('calendars.foo.urls')),

    (r'^admin/(.*)', admin.site.root),

    # Maintenance
    (r'^events/ical/(?P<area_request>)', 'calendars.events.views.icalendararea'),
    (r'^events/ical/(?P<site_request>)', 'calendars.events.views.icalendarsite'),
    (r'^events/ical/$', 'calendars.events.views.icalendar'),

    # Technicians Rota
    (r'^tech/ical/(?P<tech_request>)', 'calendars.techs.views.icalendartech'),
    (r'^techs/ical/$', 'calendars.techs.views.icalendartechs'),
)
