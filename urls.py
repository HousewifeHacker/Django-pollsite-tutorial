from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/$', 'polls.views.index', name='home'),
    url(r'^polls/(?P<poll_id>\d+)/$','polls.views.detail'),
    url(r'^polls/(?P<poll_id>\d+)/results/$','polls.views.results'),
    url(r'^polls/(?P<poll_id>\d+)/vote/$','polls.views.vote'),
    url(r'^admin/', include(admin.site.urls))
)
