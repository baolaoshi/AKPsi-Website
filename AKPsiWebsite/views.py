from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from AKPsiWebsite.forms import NewUserForm, NewRusheeForm, LoginForm
from portal.models import Rushee, User

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

def news_view(request):
	data = {}
	return render(request, 'news.html', data)

def recruitment_view(request):
	data = {}
	if request.user.is_authenticated():
		return HttpResponseRedirect("/application/")
	else:
		if request.method == 'POST':
			form = LoginForm(request.POST)
			if form.is_valid():
				cd = form.cleaned_data
				username = cd['username']
				password = cd['password']
				user = authenticate(username=username, password=password)
				if user is not None:
					login(request, user)
					return HttpResponseRedirect("/application/")
				else: 
					data['error'] = "Your email and password don't match!"
					data['form'] = LoginForm()
		else:
			data['form'] = LoginForm()
		return render(request,'recruitment.html', data, context_instance=RequestContext(request))

def signup_view(request):
	data = {}
	form = NewUserForm(request.POST)
	if form.is_valid():
		new_user = form.save()
		print form.cleaned_data['password1']
		new_rushee = Rushee(user=new_user)
		new_rushee.save()
		new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
		if new_user is not None:
			new_user.backend = 'django.contrib.auth.backends.ModelBackend'
			login(request, new_user)
		return HttpResponseRedirect("/application")
	else:
		form = NewUserForm()
	data["form"] = form
	return render(request, 'signup.html', data, context_instance=RequestContext(request))

def application_view(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/recruitment")
	data = {}

	if request.method == 'POST':
		form = NewRusheeForm(request.POST, request.FILES)
		if form.is_valid():
			cd = form.cleaned_data
			rushee = Rushee.objects.get(user=request.user)
			rushee.phone_num = cd['phone_num']
			rushee.dorm = cd['dorm']
			rushee.grad_class = cd['grad_class']
			rushee.major = cd['major']
			rushee.gpa = cd['gpa']
			rushee.q1 = cd['q1']
			rushee.q2 = cd['q2']
			rushee.q3 = cd['q3']
			rushee.q4 = cd['q4']
			rushee.picture = cd['picture']
			rushee.resume = cd['resume']
			rushee.save()
			return HttpResponseRedirect("/application")
		else:
			rushee = Rushee.objects.get(user=request.user)
			form = NewRusheeForm(initial={'phone_num' : rushee.phone_num,
										  'dorm' : rushee.dorm,
										  'grad_class' : rushee.grad_class,
										  'major' : rushee.major,
										  'gpa' : rushee.gpa,
										  'q1' : rushee.q1, 
										  'q2' : rushee.q2,
										  'q3' : rushee.q3,
										  'q4' : rushee.q4})
	else:
		rushee = Rushee.objects.get(user=request.user)
		form = NewRusheeForm(initial={'phone_num' : rushee.phone_num,
									  'dorm' : rushee.dorm,
									  'grad_class' : rushee.grad_class,
									  'major' : rushee.major,
									  'gpa' : rushee.gpa,
									  'q1' : rushee.q1, 
									  'q2' : rushee.q2,
									  'q3' : rushee.q3,
									  'q4' : rushee.q4})	
	data["form"] = form
	return render(request, 'application.html', data, context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/recruitment')