from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^calendars/', include('calendars.foo.urls')),

    (r'^admin/(.*)', admin.site.root),

    (r'^events/ical/(?P<area_request>)', 'calendars.events.views.icalendar'),
)
