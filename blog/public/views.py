from django.http import HttpResponse, HttpResponseRedirect
from blog.admin.models import Entry
from django.shortcuts import get_object_or_404, render_to_response
from google.appengine.ext import db

def index(request):
	Entries = db.GqlQuery("SELECT * FROM Entry ORDER BY created_on DESC LIMIT 5")
	
	return render_to_response('index.html',{ 'Entries': Entries })
	
def archive(request):
	return render_to_response('archive.html')
	
def about(request):
	return render_to_response('about.html')
	
def entry_detail(request, queryset, slug):
	Entries = Entry.all().filter('slug', slug)
	#Entries = db.GqlQuery("SELECT * FROM Entry WHERE slug = :slug", slug=slug)
	
	return render_to_response('entry_detail.html',{ 'Entries': Entries})