from django.shortcuts import render
from forms import LoginForm, SignupForm, PasswordChangeForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


def login(request):

	if request.method=='POST':
		form = LoginForm(request.POST)

		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username,password=password)

			if user is not None:
				auth_login(request,user)
				return HttpResponseRedirect(reverse('profile'))

	else:
		form = LoginForm()

	return render(request, 'login_form.html', {'form':form} )



def signup(request):

	if request.method=='POST':
		form = SignupForm(request.POST)

		if form.is_valid():
			pass
			
	else:
		form = SignupForm()
		
	return render(request, 'signup_form.html', {'form':form} )


def password_change(request):

	if request.method == "POST":
		form = PasswordChangeForm(request.POST)	

		if form.is_valid():
			current_password = request.POST['current_password']
			username = request.user.username
			user = authenticate(username=username,password=current_password)

			if user is not None:

				if request.POST['password1'] == request.POST['password2']:
					user.set_password(request.POST['password1'])
					user.save()
				else:
					# error message for non-matching passwords
					pass

			else:
				# error message for wrong password? 
				pass

	else:
		form = PasswordChangeForm()

	return render(request, 'password_change_form.html', {'form':form})


def logged_in(request):
	return render(request, 'logged_in.html')

def profile(request):
	return render(request, 'profile.html')
