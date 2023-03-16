from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

context = {}
context['name'] = 'Juan dela Cruz'
context['type'] = 'User'

@login_required
def dashboard(request):
    # Generate list of Eateries to be displayed in the main panel of the User Dashboard
    # Eateries should be retrieved from the database in the future
    # for i in range(5):
    #     context['eateries'].append(
    #         {
    #             'name': f'Eatery Name {i}',
    #             'genre': 'Filipino',
    #             'location': 'Area 2',
    #             'rating': 5,
    #         },
    #     )
    context['page'] = 'dashboard'
    return render(request, 'userdashboard/dashboard.html', context)

@login_required
def profile(request):
    context['page'] = 'profile'
    return render(request, 'userdashboard/profile.html', context)

@login_required
def campusmap(request):
    context['page'] = 'campusmap'
    return render(request, 'userdashboard/campusmap.html', context)

@login_required
def findeatery(request):
    context['page'] = 'findeatery'
    return render(request, 'userdashboard/findeatery.html', context)
