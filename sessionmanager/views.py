from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from userdashboard.models import Profile
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

def opensession(request):
    return render(request, 'sessionmanager/login.html')

def loginuser(request):
    return render(request, 'sessionmanager/loginuser.html')

def loginbusinessowner(request):
    return render(request, 'sessionmanager/loginbusinessowner.html')

@login_required
def loginredirect(request):
    account_type = request.user.user_profile.account_type

    if account_type == 'User':
        return redirect('userdashboard-dashboard')
    elif account_type == 'Business Owner':
        return redirect('businessdashboard-dashboard')
    else:
        return redirect('sessionmanager-opensession')

def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            account_type = form.cleaned_data.get('account_type')
            user = User.objects.filter(username=username).first()

            # Create Profile for new User
            Profile.create(user, account_type=account_type).save()

            if account_type == 'User':
                group = Group.objects.get(name="visitor")
                user.groups.add(group)
            elif account_type == 'Business Owner':
                group = Group.objects.get(name="businessowner")
                user.groups.add(group)

            messages.success(request, f'Account created for {username}!')
            return redirect('sessionmanager-opensession')
    else:
        form = UserRegisterForm()
    return render(request, 'sessionmanager/signup.html', {"form": form})
