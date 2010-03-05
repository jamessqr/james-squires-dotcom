from django.conf.urls.defaults import *

urlpatterns = patterns('public.views',
    (r'^$', 'index'),
)

from google.appengine.ext import db

# Create your models here.
    
