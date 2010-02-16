from django.http import HttpResponse, HttpResponseRedirect
from blog.admin import models
import admin_forms
from django.shortcuts import render_to_response

def index(request):
	if request.method == 'GET':
		entryform = admin_forms.EntryForm()
	if request.method == 'POST':
		entryform = admin_forms.EntryForm(request.POST)
		if entryform.is_valid():
			entry = entryform.save()
			#return render_to_response('index.html')		
	payload = dict(entryform=entryform)
	return render_to_response('index.html',payload)