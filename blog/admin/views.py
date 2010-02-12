from django.http import HttpResponse, HttpResponseRedirect
from blog.admin import models
import admin_forms
from django.shortcuts import render_to_response

def index(request):
	if request.method == 'GET':
		entryform = admin_forms.EntryForm()
	payload = dict(entryform=entryform)
	return render_to_response('index.html',payload)