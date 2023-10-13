
from django.shortcuts import render , redirect, HttpResponse

def HomePage(request):
    data={}
    if request.method == 'GET':
        name = request.GET.get('name')
        email = request.GET.get('email')
        interest = request.GET.get('interest')
        data ={'name':name, 'email':email, 'interest':interest}
       
        if name != None and email != None and interest !=None:
            
            return redirect('videoroom',data)
        else:
            return render(request, 'index.html')
    return render(request, 'index.html')

def VideoRoom(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    interest = request.GET.get('interest')
    print(name, email, interest)
    data={'name': name, 'email': email, 'interest': interest}
       
    
    
   
    return render(request, 'videocall.html',data)
