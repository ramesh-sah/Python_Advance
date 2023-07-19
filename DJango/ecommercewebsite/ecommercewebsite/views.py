from django.http import HttpResponse
from django.shortcuts import render
from submitcontact.models import submitContact
from AboutContent.models import AboutPageContent
from termsConditions.models import TermsCondition
from Refund.models import refund
from AccountSubmit.models import Accountsubmit


def Home(request):
    return render(request, 'index.html')


def Shop(request):
    return render(request, 'shop.html')


""" About us page functions start"""


def About(request):
    aboutcontentobj = AboutPageContent.objects.all()
    data = {'aboutcontentobj': aboutcontentobj}

    return render(request, 'about.html', data)


"""about us page functions end"""


""" Contact Page Functions Start """


def Contact(request):

    return render(request, 'contact.html')


def submitcontact(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        message = request.POST.get('message')
        submit = submitContact(
            first_name=fname, last_name=lname, email=email, message=message)
        submit.save()

        print(fname, lname, email, message)
    return render(request, 'index.html')


""" Contact Page Functions end"""
"""Account Section Start"""


def Account(request):

    return render(request, "account.html")


def accountsubmit(request):
    data = {}

    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        cname = request.POST.get('cname')
        country = request.POST.get('country')
        city = request.POST.get('city')
        address = request.POST.get('address')
        tel_no = request.POST.get('tel')
        phone = request.POST.get('mobile')
        submit = Accountsubmit(firstname=fname, lastname=lname,
                               company_name=cname, country=country, city=city, address=address)
        data = {'fname': fname, 'lname': lname}
        submit.save()
        print(fname, lname)
    return render(request, "account.html", data)


"""Account Section end"""


def Cart(request):
    return render(request, "cart.html")


def Changepassword(request):
    return render(request, 'change-password.html')


def Checkout(request):
    return render(request, "checkout.html")


def Orders(request):
    return render(request, "orders.html")


def Product(request):
    return render(request, "product.html")


""" refund section start"""


def Refund(request):
    refundobj = refund.objects.all()
    data = {'refundobj': refundobj}

    return render(request, "refund.html", data)


""" refund section end"""


"""terms and conditon section start"""


def Terms(request):
    termsobj = TermsCondition.objects.all()
    data = {'termsobj': termsobj}
    return render(request, "terms.html", data)


""" terms and condition section end"""
