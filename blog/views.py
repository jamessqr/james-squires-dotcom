from django.shortcuts import get_object_or_404, render_to_response
from blog.models import Entry

def entries_index(request):
	return render_to_response('blog/entry_index.html', { 'entry_list': Entry.objects.all() })
	
def archive(request):
	return render_to_response('blog/entry_archive.html')

def about(request):
	return render_to_response('blog/about.html')
