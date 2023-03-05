from django.shortcuts import render
from django.http import HttpResponse


def opensession(request):
    return render(request, 'sessionmanager/opensession.html')

def loginuser(request):
    return render(request, 'sessionmanager/loginuser.html')

def loginbusinessowner(request):
    return render(request, 'sessionmanager/loginbusinessowner.html')

def signup(request):
    return render(request, 'sessionmanager/signup.html')

