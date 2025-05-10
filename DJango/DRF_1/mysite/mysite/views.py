from django.http import HttpResponse
def Course(request):
    return HttpResponse("Welcome to wscubetech")

def About(request):
    return HttpResponse("WElcome to django ")

def courseDetails(request,courseid):
    return HttpResponse(courseid)


def courseDetailsInString(request,courseName):
    return HttpResponse(courseName)



