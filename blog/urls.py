from django.conf.urls.defaults import *
from google.appengine.ext import db
from blog.admin.models import Entry
#TODO: Import the Entry model for the url pattern

entry_info_dict = {
	'queryset': Entry.all(),
	'date_field': 'pub_date',
}

urlpatterns = patterns('',
	(r'^admin-hidden/$', 'blog.admin.views.index'),
	(r'^$', 'blog.public.views.index'),
	(r'^archive/', 'blog.public.views.archive', entry_info_dict),
	(r'^about/', 'blog.public.views.about'),
	(r'^(?P<year>\d{4})', 'blog.public.views.archive_year', entry_info_dict),
	(r'^(?P<slug>[a-zA-Z0-9_.-]+)/$', 'blog.public.views.entry_detail', entry_info_dict),
    # Example:
    # (r'^blog_app/', include('blog_app.foo.urls')),

    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),

)