from django.conf.urls.defaults import patterns, include, url, handler404, handler500
from django.views.generic import DetailView,ListView
from polls.models import Poll

urlpatterns = patterns('',
    (r'^$',
        ListView.as_view(
            queryset=Poll.objects.order_by('-pub_date')[:5],
            context_object_name='latest_poll_list',
            template_name='polls/index.html')),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Poll,
            template_name='polls/detail.html'), name='poll_detail'),
    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Poll,
            template_name='polls/results.html'),
        name='poll_results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote', name='vote'),
    url(r'^create/$', 'polls.views.create_poll', name='create'),
)

