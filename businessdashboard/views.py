from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

context = {}

@login_required
def dashboard(request):
    context['page'] = 'dashboard'
    return render(request, 'businessdashboard/dashboard.html', context)

@login_required
def profile(request):
    context['page'] = 'profile'
    return render(request, 'businessdashboard/profile.html', context)

@login_required
def businesspage(request):
    context['page'] = 'businesspage'
    return render(request, 'businessdashboard/businesspage.html', context)

@login_required
def editbusinesspage(request):
    context['page'] = 'editbusinesspage'
    return render(request, 'businessdashboard/editbusinesspage.html', context)

@login_required
def viewrating(request):
    context['page'] = 'viewrating'
    return render(request, 'businessdashboard/viewrating.html', context)