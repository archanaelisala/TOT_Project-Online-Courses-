from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


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