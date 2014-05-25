from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext

def index_view(request):
	data = {}
	return render(request, 'index.html', data, context_instance=RequestContext(request))

def about_view(request):
	data = {}
	return render(request, 'about.html', data, context_instance=RequestContext(request))


from portal.models import Brother

def brothers_view(request):
	data = {}
	active_bros = Brother.objects.filter(is_alumni=False)
	alumni_bros = Brother.objects.filter(is_alumni=True)

	# Active bros
	data['mu_class'] = active_bros.filter(pledge_class="Mu").order_by('last_name')
	data['nu_class'] = active_bros.filter(pledge_class="Nu").order_by('last_name')
	data['xi_class'] = active_bros.filter(pledge_class="Xi").order_by('last_name')
	data['omicron_class'] = active_bros.filter(pledge_class="Omicron").order_by('last_name')
	data['pi_class'] = active_bros.filter(pledge_class="Pi").order_by('last_name')
	data['rho_class'] = active_bros.filter(pledge_class="Rho").order_by('last_name')
	data['sigma_class'] = active_bros.filter(pledge_class="Sigma").order_by('last_name')

	# Alumni bros
	data['grad_2005'] = alumni_bros.filter(grad_class="2005").order_by('last_name')
	data['grad_2006'] = alumni_bros.filter(grad_class="2006").order_by('last_name')
	data['grad_2007'] = alumni_bros.filter(grad_class="2007").order_by('last_name')
	data['grad_2008'] = alumni_bros.filter(grad_class="2008").order_by('last_name')
	data['grad_2009'] = alumni_bros.filter(grad_class="2009").order_by('last_name')
	data['grad_2010'] = alumni_bros.filter(grad_class="2010").order_by('last_name')
	data['grad_2011'] = alumni_bros.filter(grad_class="2011").order_by('last_name')
	data['grad_2012'] = alumni_bros.filter(grad_class="2012").order_by('last_name')
	data['grad_2013'] = alumni_bros.filter(grad_class="2013").order_by('last_name')
	data['grad_2014'] = alumni_bros.filter(grad_class="2014").order_by('last_name')

	return render(request,'brothers.html', data, context_instance=RequestContext(request))