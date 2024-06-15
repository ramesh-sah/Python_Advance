# from django.http import HttpResponse
# def course(request):
#     return HttpResponse("course")

# def aboutus(request):
#     return HttpResponse("aboutus")

# def courseDetails(request,courseid):
#     return HttpResponse(courseid)

# def courseNames(request,courseName):
#     return HttpResponse(courseName)

# def courseDetailsInSlug(request,courseSlug):
#     return HttpResponse(courseSlug) 

from django.http import HttpResponse
from django.shortcuts import render
def homePage(request):
    data={
        'title':'homepage new'
    }
    return render(request, 'index.html',data)


