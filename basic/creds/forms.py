from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)


class PasswordChangeForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        if self.cleaned_data['password2'] != self.cleaned_data['password1']:
            raise forms.ValidationError('Passwords must match')
        return self.cleaned_data


class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField()


class SignupForm(forms.ModelForm):
    username = forms.CharField(max_length=255)
    email1 = forms.EmailField()
    email2 = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        if self.cleaned_data['password2'] != self.cleaned_data['password1']:
            raise forms.ValidationError('Passwords must match')
        return self.cleaned_data

    def clean(self):
        if self.cleaned_data['email2'] != self.cleaned_data['email1']:
            raise forms.ValidationError('Email addresses must match')
        return self.cleaned_data

    def clean_email2(self):
        # here
        if User.objects.get(email=email1):
          raise forms.ValidationError('This email address is already in use')

    def clean_username(self):
        # here
        if User.objects.get(username=username):
          raise forms.ValidationError('This username is already taken')


    class Meta:
        model = User
        fields = ['username', 'email1', 'email2', 'password1', 'password2']

class PasswordResetForm(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        if self.cleaned_data['password2'] != self.cleaned_data['password1']:
            raise forms.ValidationError('Passwords must match')
        return self.cleaned_data