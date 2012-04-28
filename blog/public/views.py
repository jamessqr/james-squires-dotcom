from django.http import HttpResponse, HttpResponseRedirect
from blog.admin import models
from django.shortcuts import render_to_response

def index(request):
	return render_to_response('index.html')
	
def archive(request):
	return render_to_response('archive.html')
	
def about(request):
	return render_to_response('about.html')