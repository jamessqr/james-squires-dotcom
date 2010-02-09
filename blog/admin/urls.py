from django.conf.urls.defaults import *

urlpatterns = patterns('admin.views',
    (r'^$', 'index'),
)

from google.appengine.ext import db

# Create your models here.
    
