from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Eatery
from userdashboard.forms import UserUpdateForm, ProfileUpdateForm
from django.core.paginator import Paginator
from django.contrib import messages


context = {}

@login_required
def dashboard(request):
    context['page'] = 'dashboard'
    return render(request, 'userdashboard/dashboard.html', context)

@login_required
def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.user_profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('userdashboard-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.user_profile)

    context['page'] = 'profile'
    context['u_form'] = u_form
    context['p_form'] = p_form

    return render(request, 'userdashboard/profile.html', context)

@login_required
def campusmap(request):
    context['page'] = 'campusmap'
    return render(request, 'userdashboard/campusmap.html', context)

@login_required
def findeatery(request):
    context['page'] = 'findeatery'
    return render(request, 'userdashboard/findeatery.html', context)
    
class EateryListView(ListView):
    model = Eatery
    template_name = 'userdashboard/findeatery.html'
    context_object_name = 'eateries'
    paginate_by = 6
    ordering = ['eatery_name']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        location = self.request.GET.get('location')
        food_genre = self.request.GET.get('food_genre')

        
        if query:
            queryset = queryset.filter(eatery_name__icontains=query)
        if location:
            queryset = queryset.filter(location__icontains=location)
        if food_genre:
            queryset = queryset.filter(food_genre__icontains=food_genre)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_term'] = self.request.GET.get('q')
        context['location'] = self.request.GET.get('location')
        context['food_genre'] = self.request.GET.get('food_genre')
        return context

