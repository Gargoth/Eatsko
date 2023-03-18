from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . models import Eatery
from django.views.generic import ListView


context = {}
context['name'] = 'Juan dela Cruz'
context['type'] = 'User'

@login_required
def dashboard(request):
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
    if request.method == "POST":
        searched = request.POST['searched']
        eatery_search = Eatery.objects.filter(eatery_name__icontains=searched)
	
        return render(request, 'userdashboard/findeatery.html', {'searched':searched, 'eateries':eatery_search})
    
    else:
         return render(request, 'userdashboard/findeatery.html', {'eateries':Eatery.objects.all()})
    

class EateryListView(ListView):
        
	model = Eatery
	paginate_by = 10
	template_name = 'userdashboard/findeatery.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['eatery'] = Eatery.objects.all()
		return context