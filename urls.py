from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^maintenance/', include('maintenance.foo.urls')),

    # Uncomment this for admin:
    (r'^admin/(.*)', admin.site.root),

    (r'^events/$', 'maintenance.events.views.index'),
)
