from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^admin/$', 'blog.admin.views.index'),
	(r'^$', 'blog.public.views.index'),
	(r'^archive/', 'blog.public.views.archive'),
	(r'^about/', 'blog.public.views.about'),
    # Example:
    # (r'^blog_app/', include('blog_app.foo.urls')),

    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),

)
