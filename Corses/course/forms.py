from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm


class UserReg(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Enter password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Enter Confirm password", }))

    class Meta:
        model = User
        fields = ['username'] #this is my user table with username and password and confirm password kM?
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter username", "requires": True, }),
        }


        


# class UsRegg(forms.ModelForm):
#     username = forms.CharField()
#     password1 = forms.CharField(widget=forms.PasswordInput(
#         attrs={"class": "form-control", "placeholder": "Enter password"}))
#     password2 = forms.CharField(widget=forms.PasswordInput(
#         attrs={"class": "form-control", "placeholder": "Enter Confirm password", }))
#     #for me these are default fields... 

#     #now for additional fields
#     class Meta:
#         model = course
#         fields = ['username','password1','password2','course_name']
#         widgets = {
#                 "course_name" : forms.TextInput(attrs={'class':"form-control","placeholder":"Enter course_name"})
#         }

class Uprofile(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

        widgets = {
        "username" : forms.TextInput(attrs={"class":'form-control','readonly':True}),
        "first_name" : forms.TextInput(attrs={"class":'form-control','placeholder':'Update first_name'}),
        "last_name" : forms.TextInput(attrs={"class":'form-control','placeholder':'Update last_name'}),
        "email" : forms.TextInput(attrs={"class":'form-control','placeholder':'Update email'})
        }