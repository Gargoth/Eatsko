from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from . models import Eatery
from django.core.paginator import Paginator


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
    context['page'] = 'findeatery'
    if request.method == "POST":
        searched = request.POST['searched']
        eateries_list = Eatery.objects.filter(eatery_name__icontains=searched)
        context['searched'] = searched
    else:
        eateries_list = Eatery.objects.all()

    paginator = Paginator(eateries_list, 6) # 6 eateries per page
    page = request.GET.get('page') # Get current page number
    eateries = paginator.get_page(page) # Get eateries for current page
    context['eateries'] = eateries
    return render(request, 'userdashboard/findeatery.html', context)
    

class EateryListView(ListView):
        
	model = Eatery
	paginate_by = 10
	template_name = 'userdashboard/findeatery.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['eatery'] = Eatery.objects.all()
		return context
