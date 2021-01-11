from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Customer


class UserReg(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Enter password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Enter Confirm password", }))

    class Meta:
        model = User
        fields = ['username']
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter username", "requires": True, })
        }


class CustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': "Enter Username", 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': "Password here  ***", 'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': "Enter Email", 'class': 'form-control'}))

    class Meta:
        model = Customer
        fields = ["username", "password", "email", "full_name"]
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Full name"}),
            "address": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Address"}),
        }

    def clean_username(self):
        uname = self.cleaned_data.get("username")
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError(
                "Customer with this username already exists.")
