from django.shortcuts import get_object_or_404, render_to_response
from blog.models import Entry

def entries_index(request):
	return render_to_response('blog/entry_index.html', { 'entry_list': Entry.objects.order_by('-pub_date')[:10] })
	
def archive(request):
	return render_to_response('blog/entry_archive.html')

def archive_2012(request):
	return render_to_response('blog/entry_archive_2012.html', { 'entry_list': Entry.objects.all })

def archive_2013(request):
	return render_to_response('blog/entry_archive_2013.html', { 'entry_list': Entry.objects.all })

def archive_2014(request):
	return render_to_response('blog/entry_archive_2014.html', { 'entry_list': Entry.objects.all })

def about(request):
	return render_to_response('blog/about.html')
