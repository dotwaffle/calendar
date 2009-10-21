from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^maintenance/', include('maintenance.foo.urls')),

    # Uncomment this for admin:
    (r'^admin/(.*)', admin.site.root),

    # (r'^events/network.ical$', 'maintenance.events.views.network'),
    (r'^events/(?P<area_request>)', 'maintenance.events.views.calendar'),
)
