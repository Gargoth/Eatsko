from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from userdashboard.models import Profile


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
            account_type = form.cleaned_data.get('account_type')

            # Create Profile for new User
            Profile.create(User.objects.filter(username=username, account_type=account_type).first()).save()

            messages.success(request, f'Account created for {username}!')
            return redirect('sessionmanager-opensession')
    else:
        form = UserRegisterForm()
    return render(request, 'sessionmanager/signup.html', {"form": form})

