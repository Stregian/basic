from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
	username = forms.CharField(max_length=255)
	password = forms.CharField(widget=forms.PasswordInput)


class PasswordChangeForm(forms.Form):
	current_password = forms.CharField(widget=forms.PasswordInput)
	password1 = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(widget=forms.PasswordInput)


class PasswordResetStart(forms.Form):
	email = forms.EmailField()


class SignupForm(forms.ModelForm):
	username = forms.CharField(max_length=255)
	email1 = forms.EmailField()
	email2 = forms.EmailField()
	password1 = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email1', 'email2', 'password1', 'password2']

