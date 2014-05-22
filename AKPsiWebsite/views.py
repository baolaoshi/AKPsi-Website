from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext

def index_view(request):
	data = {}
	return render(request, 'index.html', data, context_instance=RequestContext(request))

def about_view(request):
	data = {}
	return render(request, 'about.html', data, context_instance=RequestContext(request))