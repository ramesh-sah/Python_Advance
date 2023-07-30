from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from signupdata.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def Signup(request):
    if request.method == "POST":
        username = request.POST.get('name')
        useremail = request.POST.get("email")
        userpassword = request.POST.get("password")
        en = User(name=username, email=useremail, password=userpassword)
        en.save()
        print(useremail, username, userpassword)
        return render(request, "login.html")
    else:
        print("invalid")
    return render(request, 'signup.html')


def Login(request):
    if request.method == "POST":
        useremail = request.POST.get("email")
        userpassword = request.POST.get("password")
        User = authenticate(request, email=useremail, password=userpassword)

        if (request.User.is_authenticated):
            return HttpResponse("you r successfully login")
        else:
            print("invalid 1")

    return render(request, "login.html")
