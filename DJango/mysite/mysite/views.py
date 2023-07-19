from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import userForms


def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'Contact.html')


def about(request):
    if request.method == "GET":
        output = request.GET.get('output')
        print(output)

    return render(request, 'About.html', {'output': output})


def userForm(request):
    finalans = 0,
    data = {}

    try:
        if request.method == 'GET':

            # n1 = int(request.GET['num1'])
            # n2 = int(request.GET['num2'])
            # print(n1+n2)
            n1 = int(request.GET.get('num1'))
            n2 = int(request.GET.get('num2'))
            print(n1+n2)
            finalans = n1+n2
            data = {'n1': n1, 'n2': n2, 'output': finalans}
            url = "about?output ={}".format(finalans)
            return HttpResponseRedirect(url)

    except:
        pass
    return render(request, 'userform.html', data)


def submitForm(request):
    if request.method == 'GET':

        # n1 = int(request.GET['num1'])
        # n2 = int(request.GET['num2'])
        # print(n1+n2)
        n1 = int(request.GET.get('num1'))
        n2 = int(request.GET.get('num2'))
        print(n1+n2)
        finalans = n1+n2
        data = {'n1': n1, 'n2': n2, 'output': finalans}
        url = "about?output ={}".format(finalans)
        return HttpResponse(finalans)


def userform(request):
    finalans = 0
    fn = userForm()
    data = {'form': fn}
    try:
        if request.method == 'GET':
            n1 = int(request.GET.get('num1'))
            n2 = int(request.GET.get('num2'))
            finalans = n1+n2
            data = {
                'form': fn,
                'output': finalans
            }
            url = 'about?output={}'.format(finalans)
    except:
        pass
    return HttpResponse(finalans)


def Calculator(request):
    n1 = int(request.GET.get('num1'))
    n2 = int(request.GET.get('num2'))
    opr = request.GET.get('opr')
    print(n1, n1, opr)
    result
    try:
        if (opr == '+'):
            result = n1+n2
        elif (opr == "-"):
            result = n1 - n2
        elif (opr == "*"):
            result = n1 * n2
        elif (opr == "/"):
            result = n1/n2
    except:
        print("invalid opr")
    return render(request, 'calculator.html', {'result': result})


def OddEven(request):
    result = ''
    if request.method == 'GET':
        n1 = int(request.GET.get('num1'))
        print(n1)

        try:
            if (n1 % 2 == 0):
                result = "even number"
            else:
                result = "odd number"
        except:
            print("invalid input")
    return render(request, 'oddeven.html', {'result': result})


def Marksheet(request):
    name = ""
    english = 0
    maths = 0
    science = 0
    computerscience = 0
    socialstudies = 0
    total = 0
    percentage = 0
    grade = ""
    data = {}
    if request.method == "POST":
        name = request.POST.get('name')
        english = int(request.POST.get("english"))
        maths = int(request.POST.get("maths"))
        science = int(request.POST.get("science"))
        computerscience = int(request.POST.get("computerscience"))
        socialstudies = int(request.POST.get("socialstudies"))

    try:
        if (english < 100, maths < 100, science < 100, computerscience < 100, socialstudies < 100):
            total = english+maths+science+computerscience+socialstudies
            percentage = total*100/500

            if (percentage <= 100 and percentage >= 80):
                grade = "A Grade"
            elif (percentage < 80 and percentage >= 60):
                grade = "B Grade"
            elif (percentage < 60 and percentage >= 40):
                grade = "C Grade"
            elif (percentage < 40 and percentage >= 20):
                grade = "D Grade"
            else:
                grade = "E Grade"
        print(name, english, maths, science, computerscience,
              socialstudies, total, percentage, grade)
        data = {'name': name, 'english': english, 'maths': maths, 'science': science, 'computerscience': computerscience,
                'socialstudies': socialstudies, 'total': total, 'percentage': percentage, 'grade': grade}

    except:
        print("Invalid")

    return render(request, "marksheet.html", data)
