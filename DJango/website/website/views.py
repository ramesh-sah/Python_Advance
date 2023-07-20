from django.http import HttpResponse, request
from django.shortcuts import render
from service.models import Service
from news.models import News
from django.core import paginator
from django.core.paginator import Paginator
from saveHome.models import savehome
from django.core.mail import send_mail, EmailMultiAlternatives


def home(request):
    # send_mail('testing mail',
    #           'here is the mail',
    #           'rameshk.sah@patancollege.edu.np',
    #           ['rsah3798@gmail.com'],
    #           fail_silently=False)

    newsData = News.objects.all()

    serviceData = Service.objects.all().order_by('id')
    paginator = Paginator(serviceData, 2)
    page_number = request.GET.get('page')
    serviceDataFinal = paginator.get_page(page_number)

    # data = {'serviceData': serviceData, 'newsData': newsData}
    data = {}
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST['name']
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        message = request.POST.get('message')
        data = {'email': email, 'name': name, 'phone': phone,
                'address': address, 'message': message}
        print(email, name, phone, address, message)
        # en = savehome(email=email, name=name, phone=phone,
        #               address=address, message=message)
        # en.save()
        subject = 'tesing mail'
        from_email = "rameshk.sah@patancollege.edu.np"
        msg = '<p> welcome to <b> wscubetech</b> </p>',
        MSG = EmailMultiAlternatives(subject, msg, from_email, [email])
        MSG.content_subtype = 'html'
        MSG.send()
    else:
        print("Invalid")
    return render(request, 'index.html', data)


def newsDetails(request, slug):
    newsDetails = News.objects.get(news_slug=slug)
    data = {'newsDetails': newsDetails}
    return render(request, 'newsDetails.html', data)


def searchFilter(request):
    newsdata = News.objects.all()

    if request.method == "GET":
        st = request.GET.get('search')
        print(st)
        if st != None:
            newsdata = News.objects.filter(news_title=st)
    data = {'newsdata': newsdata}

    return render(request, 'searchfiter.html', data)


def signup(request):
    data = {}
    if request.method == "POST":
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        phone1 = request.POST.get('phone')
        password1 = request.POST.get('password')
        address1 = request.POST.get('address')
        data = {'name': name1, 'email': email1, 'phone': phone1,
                'password': password1, 'address': address1}
        print(name1, email1, phone1, password1, address1)
    return render(request, "Signup.html", data)


def login(request):
    data = {}
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = {'email': email, 'password': password}
        print(email, password)

    return render(request, 'Login.html')


def about(request):

    return render(request, "About.html")
