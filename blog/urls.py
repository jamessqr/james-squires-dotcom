from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^admin/$', 'blog.admin.views.index'),
    # Example:
    # (r'^blog_app/', include('blog_app.foo.urls')),

    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),

)
