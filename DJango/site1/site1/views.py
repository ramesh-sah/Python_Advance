from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import AbstractBaseUser

# Create your views here.

def home(request):
    data={
        'title':' this is home page',
        'bdata':'this is bdata',
        'clist':['python','java','php','c++'],
        'student_details':[
            {'name':'sachin','city':'pune'},
            {'name':'sachin','city':'pune'},
            {'name':'sachin','city':'pune'},
        ]
    }
    return render(request,'index.html',data)


def course(request):
    
    return HttpResponse("welcome to wscubetech");


def aboutus(request):
    return HttpResponse("about us");


def courseDetails(request,courseid):
    return HttpResponse(courseid);

def courseDetailsInString(request,courseName):
    return HttpResponse(courseName)

def courseDetailsInSlug(request,courseSlug):
    return HttpResponse(courseSlug)

