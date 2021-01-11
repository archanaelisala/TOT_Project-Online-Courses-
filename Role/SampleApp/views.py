from django.shortcuts import render,redirect
from SampleApp.forms import UsReg
from django.contrib import messages
# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')



def contact(request):
	return render(request,'html/contact.html')


def register(request):
	if request.method == 'POST':
		y = UsReg(request.POST)
		if y.is_valid():
			y.save()
			messages.success(request,"Your Registration is successfull")
			return redirect('/login')
	y = UsReg()
	return render(request,'html/register.html',{'y':y})


def dashboard(request):
	return render(request,'html/dashboard.html')


