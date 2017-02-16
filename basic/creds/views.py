from django.shortcuts import render
from forms import LoginForm, SignupForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


# renders a form, which if correct and complete, sends the user to a logged in page. 
def login(request):

	if request.method=='POST':
		form = LoginForm(request.POST)

		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username,password=password)

			if user is not None:
				auth_login(request,user)
				return HttpResponseRedirect(reverse('logged_in'))

	else:
		form = LoginForm()

	return render(request, 'login_form.html', {'form':form} )


def logged_in(request):

	return render(request, 'logged_in.html')


# renders a form, which if valid, registers a user to the site 
def signup(request):

	if request.method=='POST':
		form = SignupForm(request.POST)

		if form.is_valid():
			email_check = False
			
			if 


	else:
		form = SignupForm()
		
	return render(request, 'signup_form.html', {'form':form} )