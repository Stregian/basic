from django.shortcuts import render
from django import forms
from forms import LoginForm, SignupForm, PasswordChangeForm, PasswordResetRequestForm, PasswordResetForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


def success(request, url, message=None):

    return render(request, 'success.html', {
        'url':url,
        'message':message,
        } )


def login(request):

    if request.method=='POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])

            if user:
                auth_login(request,user)
                return HttpResponseRedirect(reverse('profile'))

    else:
        form = LoginForm()

    return render(request, 'login_form.html', {'form':form} )


def signup(request):

    if request.method=='POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            print(cd['username'])


            new_user = User.objects.create_user(username=cd['username'],
                                        email=cd['email1'],
                                        password=cd['password1'],
                )
            new_user.save()
            message = 'User successfully created, log in by clicking the link below'
            url = reverse('login')
            return success(request, url, message)

    else:
        form = SignupForm()
        
    return render(request, 'signup_form.html', {
        'form':form,
        'form_title': 'Sign up',
        'action': reverse('signup'),
        })


@login_required
def password_change(request):

    if request.method == "POST":
        
        form = PasswordChangeForm(request.POST) 

        if form.is_valid():
            
            cd = form.cleaned_data
            user = authenticate(username=request.user.username, password=cd['current_password'])

            if not user:
                form.errors['__all__'] = form.error_class(['Current password incorrect'])

            else:
                user.set_password(cd['password1'])
                user.save()
                update_session_auth_hash(request, user)

                # Success !
                message = "You have successfully changed your password"
                url = reverse('profile')
                return success(request, url, message)

    else:
        form = PasswordChangeForm()

    return render(request, 'password_change_form.html', {
        'form':form,
        'form_title': 'Change Password',
        'action': reverse('password-change')
        })


def password_reset_request(request):

    if request.method == "POST":
        form = PasswordResetRequestForm(request.POST)

        user = User.objects.get(email=request.POST['email'])
        if not user:
            form.errors['__all__'] = form.error_class(['No users with this email address'])

        if (form.is_valid()):

            body_message = render(request,'password_reset_email.html', {
                'domain':get_current_site(request).domain,
                'uid':urlsafe_base64_encode(force_bytes(user.id)),
                'token':default_token_generator.make_token(user),
                'user':user.username,
                })

            print(body_message)
            email_message = EmailMessage("Password reset",body_message,[request.POST['email']])
            email_message.send()
            return render(request,'password_reset_email_sent.html')

    else:
        form = PasswordResetRequestForm()

    return render(request, 'password_reset_request.html', {
        'form':form, 
        'form_title': 'Reset', 
        'action': reverse('password-reset-request')
        })


def password_reset(request, uid, token):
    user = User.objects.get(id=urlsafe_base64_decode(uid))

    if request.method == "POST":
        form = PasswordResetForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user.set_password(cd['password1'])
            user.save()

            url = reverse('login')
            message = 'You have changed your password. You can sign in with your new password now.'
            return success(request, url, message)

    else:
        form = PasswordResetForm()

    return render(request, 'password_reset_form.html', {
        'form':form,
        'user':user,
        })


def logged_in(request):
    return render(request, 'logged_in.html')

def profile(request):
    return render(request, 'profile.html')
