from django.shortcuts import render, redirect
from NewApp.forms import UserReg
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'NewApp/home.html')


def about(request):
    return render(request, 'NewApp/about.html')


def contact(request):
    return render(request, 'NewApp/contact.html')


def register(request):
    if request.method == "POST":
        data = UserReg(request.POST)
        if data.is_valid():
            data.save()
            username = data.cleaned_data.get('username')
            messages.success(
                request, "hii {} you are successfully registered".format(username))
            return redirect("login")
        # return HttpResponse("done")
    else:
        data = UserReg()
        return render(request, 'NewApp/register.html', {'data': data})
