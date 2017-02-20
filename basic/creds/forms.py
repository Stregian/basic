from django import forms
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


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


class EmailChangeForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput)
    email1 = forms.EmailField()
    email2 = forms.EmailField()

    def clean(self):
        if self.cleaned_data['email2'] != self.cleaned_data['email1']:
            raise forms.ValidationError('Email addresses must match')
        return self.cleaned_data


class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField()


class SignupForm(forms.ModelForm):
    username = forms.CharField(max_length=255)
    email1 = forms.EmailField()
    email2 = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()


    def clean(self):
        if self.cleaned_data['password2'] != self.cleaned_data['password1']:
            raise forms.ValidationError('Passwords must match')

        if self.cleaned_data['email2'] != self.cleaned_data['email1']:
            raise forms.ValidationError('Email addresses must match')
        return self.cleaned_data
        
        try:
            user = User.objects.get(email=email1)
            raise forms.ValidationError('User already exists')
        except:
            user = None

        try:
            user = User.objects.get(email=email1)
            raise forms.ValidationError('Email already in use')
        except:
            user = None

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