from django.http import HttpResponse, HttpResponseRedirect
from blog.admin import models
from django.shortcuts import render_to_response
from google.appengine.ext import db

def index(request):
	Entries = db.GqlQuery("SELECT * FROM Entry ORDER BY created_on DESC LIMIT 5")
	
	return render_to_response('index.html',{ 'Entries': Entries })
	
def archive(request):
	return render_to_response('archive.html')
	
def about(request):
	return render_to_response('about.html')