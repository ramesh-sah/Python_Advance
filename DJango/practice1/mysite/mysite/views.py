from django.http import HttpResponse
from django.shortcuts import render 
def course(request,course_id):
    return HttpResponse(str(course_id)+"welcome to ws")
def about(request):
    return HttpResponse("welcome to wscubetech")

def homepage(request):
    data={
        'title':"homePage new",
        
    }
    return render(request,"index.html",data)



    
    