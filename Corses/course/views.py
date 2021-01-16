from django.shortcuts import render, redirect
from django.http import HttpResponse
from course.forms import UserReg,Uprofile
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Course_details,Course_Content


# Create your views here.


def home(request):
    return render(request, 'mycourse/home.html')

def course(request):
    data = Course_details.objects.all()
    return render(request, 'mycourse/course.html',{'data':data})


def contact(request):
    return render(request, 'mycourse/contact.html')


def register(request):
    if request.method == "POST":
        data = UserReg(request.POST)
        if data.is_valid():
            c = data.save()
            #username = data.cleaned_data.get('username')
            c.save()
            messages.success(request, "hii you are successfully registered")
            return redirect("/login")
    else:
        data = UserReg()
        return render(request, 'mycourse/register.html', {'data': data})


def addcourse(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES['Picture']
        description = request.POST.get('description')
        Course_details.objects.create(title=title,image=image,description=description)
        return redirect('addcourse')
    return render(request,'mycourse/addcourse.html')


def mycourses(request):
    return render(request,'mycourse/mycourses.html')


def profile(request):
    return render(request,'mycourse/profile.html')


def update_user(request):
    if request.method == 'POST':
        t = Uprofile(request.POST,instance=request.user)
        if t.is_valid():
            t.save()
            messages.success(request,"updated successfully")
            return redirect('/profile')
    t = Uprofile(instance=request.user)
    return render(request,'mycourse/update.html',{'t':t})


#change password with old password
def changepassword(request):
    if request.method == 'POST':
        p = PasswordChangeForm(user = request.user,data=request.POST)
        if p.is_valid():
            update_session_auth_hash(request,p.user)
            return redirect('profile')
    else:
        p = PasswordChangeForm(user=request.user)
    return render(request,'mycourse/change_password.html',{'form':p})



def upload_course_content(request):
    if request.method == 'POST': 
         
        video = request.POST.get('video')
        theory = request.POST.get('theory')
        Course_Content.objects.create(video=video,theory=theory)

        #content = Course_Content(video=video,theory=theory)
        #content.save()
        return redirect('course')
     
    return render(request,'mycourse/upload_course_content.html')
    #return render(request,'mycourse/upload_course_content.html')



def Content(request):
    content = Course_Content.objects.all()
    return render(request,'mycourse/content.html',{'content':content})



     
    







