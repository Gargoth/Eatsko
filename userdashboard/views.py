from django.shortcuts import render
from django.http import HttpResponse

context = {
    'name': 'Juan dela Cruz',
    'type': 'User',
    'eateries': [
            {
                'name': 'Eatery Name',
                'genre': 'Filipino',
                'location': 'Area 2',
                'rating': 5,
            },
            {
                'name': 'Eatery Name',
                'genre': 'Filipino',
                'location': 'Area 2',
                'rating': 5,
            },
            {
                'name': 'Eatery Name',
                'genre': 'Filipino',
                'location': 'Area 2',
                'rating': 5,
            },
            {
                'name': 'Eatery Name',
                'genre': 'Filipino',
                'location': 'Area 2',
                'rating': 5,
            },
            {
                'name': 'Eatery Name',
                'genre': 'Filipino',
                'location': 'Area 2',
                'rating': 5,
            },
            {
                'name': 'Eatery Name',
                'genre': 'Filipino',
                'location': 'Area 2',
                'rating': 5,
            },
        ],
}

def dashboard(request):
    return render(request, 'userdashboard/dashboard.html', context)

def profile(request):
    return render(request, 'userdashboard/profile.html', context)

def campusmap(request):
    return render(request, 'userdashboard/campusmap.html', context)

def findeatery(request):
    return render(request, 'userdashboard/findeatery.html', context)
