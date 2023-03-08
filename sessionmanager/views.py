from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm


def opensession(request):
    return render(request, 'sessionmanager/opensession.html')

def loginuser(request):
    return render(request, 'sessionmanager/loginuser.html')

def loginbusinessowner(request):
    return render(request, 'sessionmanager/loginbusinessowner.html')

def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('sessionmanager-opensession')
    else:
        form = UserRegisterForm()
    return render(request, 'sessionmanager/signup.html', {"form": form})

