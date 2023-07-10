from django.http import HttpResponse
from django.shortcuts import render
def homePage(request):
    data={
        'title':'home new',
        'bdata':'welcome to django',
        'clist':['php','java','django'],
        'student_details':[
            {'name':'pradeep',"no":9862981898},
            {'name':'testing','no':9865985898}
        ]

    }
    return render(request,"index.html",data)

def about_us(request):
    return HttpResponse("hello to django")

def courses_in(request):
    return HttpResponse("this is courses")

def courseDetails(request,courseid):
    return HttpResponse(courseid) 

def courseDetailsInString(request,courseName):
    return HttpResponse(courseName)

def courseDetailsInSlug(request,courseSlug):
    return HttpResponse(courseSlug)