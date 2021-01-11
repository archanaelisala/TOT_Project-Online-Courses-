from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm	
from django import forms

class UsReg(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(
	    attrs={"class": "form-control", "placeholder": "Enter password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(
	    attrs={"class": "form-control", "placeholder": "Enter Confirm password", }))
	class Meta:
		model =User
		fields = ['username','email']
		widgets = {
		"username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter username", "requires": True, }),
		"email": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Email", "requires": True, }),

		}