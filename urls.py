from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.base import TemplateView 
from django.views.generic import DetailView, DateDetailView
from blog.models import Entry
from blog.feeds import LatestEntriesFeed
admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

entry_info_dict = {
	'queryset': Entry.objects.all(),
	'date_field': 'pub_date',
}

urlpatterns = patterns('',
    (r'^_ah/warmup$', 'djangoappengine.views.warmup'),
	(r'^admin/', include(admin.site.urls)),
	(r'^$', 'blog.views.entries_index'),
	(r'^archive/2014', 'blog.views.archive_2014'),
	(r'^archive/2013', 'blog.views.archive_2013'),
	(r'^archive/2012', 'blog.views.archive_2012'),
	(r'^archive/', 'blog.views.archive'),
	(r'^about/', 'blog.views.about'),	
	(r'^feed/$', LatestEntriesFeed()),
	(r'^(?P<slug>[a-zA-Z0-9_.-]+)/$', DetailView.as_view(model=Entry)),
	(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[0-9A-Za-z-]+)/$',
			DateDetailView.as_view(slug_field='slug', month_format='%m', **entry_info_dict)),
)
