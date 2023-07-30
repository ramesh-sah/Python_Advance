from django.shortcuts import render, redirect


def Index(request):
    return render(request, 'index.html')


def About(request):
    return render(request, 'about.html')


def AndroidAppDevelopmentNepal(request):
    return render(request, 'andrioid-app-development-nepal.html')
