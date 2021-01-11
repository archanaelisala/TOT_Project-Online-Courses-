from django.shortcuts import render,redirect
from myhospital.models import UserDetails
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from myhospital.forms import UserReg
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from HospitalManagement import settings
from django.core.mail import send_mail

# Create your views here.
def nav(request):
	return render(request,'myhospital/navbar.html')

def home(request):
	return render(request,'myhospital/home.html')

def about(request):
	return render(request,'myhospital/about.html')

def register(request):
	# if request.method == 'POST':
	# 	Firstname = request.POST.get('fname')
	# 	Lastname = request.POST.get('lname')
	# 	Username = request.POST.get('username')
	# 	Password = request.POST.get('password')
	# 	Address = request.POST.get('address')
	# 	Mobile = request.POST.get('mobile')
	# 	#Image = request.POST.get('profilepic')
	# 	UserDetails.objects.create(Firstname=Firstname,Lastname=Lastname,Username=Username,Password=Password,Address=Address,Mobile=Mobile)
	# 	return redirect('login')
	# return render(request,'myhospital/register.html')
	if request.method == "POST":
		data = UserReg(request.POST)
		if data.is_valid():
			data.save()
			username = data.cleaned_data.get('username')
			messages.success(request, "hii {} you are successfully registered".format(username))
		return redirect("login")
	else:
		data = UserReg()
		return render(request, 'myhospital/register.html', {'data': data})



# def login(request):
# 	if request.method == "POST":
# 		username = request.POST.get('uname')
# 		password = request.POST.get('pwd')


# 		user = UserDetails.objects.all().filter(Username=username,Password=password)

# 		# if user:
# 		# 	#return redirect('home')
# 		# 	pass
# 		# else:
# 		# 	return redirect("login")
# 		#return redirect('nav')
# 	return render(request,'myhospital/login.html')




@login_required
def addpatient(request):
	return render(request,'myhospital/addpatient.html')