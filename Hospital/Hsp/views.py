from django.shortcuts import render, redirect
from Hsp.forms import UserReg
from django.contrib import messages
from .models import Patient
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'hsp/home.html')


def about(request):
    return render(request, 'hsp/about.html')


def contact(request):
    return render(request, 'hsp/contact.html')


def register(request):
    if request.method == "POST":
        data = UserReg(request.POST)
        if data.is_valid():
            data.save()
            username = data.cleaned_data.get('username')
            messages.success(
                request, "hii {} you are successfully registered".format(username))
            return redirect("login")
    else:
        data = UserReg()
        return render(request, 'hsp/register.html', {'data': data})

@login_required
def AddPatient(request):
    if request.method == 'POST':
        Firstname = request.POST.get('fname')
        Lastname = request.POST.get('lname')
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        Address = request.POST.get('address')
        Mobile = request.POST.get('mobile')
        Symptoms = request.POST.get('symptoms')
        Patient.objects.create(Firstname=Firstname,Lastname=Lastname,Username=Username,Password=Password,Address=Address,Mobile=Mobile,Symptoms=Symptoms)
        return render(request,'Hsp/addpatient_Details.html')
    return render(request,'Hsp/addpatient_Details.html')


@login_required
def ViewAllPatientsList(request):
    data = Patient.objects.all()
    return render(request,'Hsp/ViewAllPatientsList.html',{'data':data})