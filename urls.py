from django.conf.urls.defaults import patterns, include, url, handler404, handler500

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls'),),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls))
)
