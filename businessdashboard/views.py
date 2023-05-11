from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Menu

context = {}



@login_required
def dashboard(request):
    context = {
        'menu': Menu.objects.all()
    }
    return render(request, 'businessdashboard/dashboard.html', context)

class MenuListView(ListView):
    model = Menu
    template_name = 'businessdashboard/businesspage.html'
    context_object_name = 'menu'
    ordering = ['-date_posted']

class EditMenuListView(ListView):
    model = Menu
    template_name = 'businessdashboard/editbusinesspage.html'
    context_object_name = 'menu'
    ordering = ['-date_posted']

class MenuDetailView(DetailView):
    model = Menu
    context_object_name = 'menu'

class MenuCreateView(LoginRequiredMixin, CreateView):
    model = Menu
    fields = ['title', 'content', 'price']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MenuUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Menu
    fields = ['title', 'content', 'price']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        menu = self.get_object()
        if self.request.user == menu.author:
            return True
        return False


class MenuDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Menu
    success_url = '/'

    def test_func(self):
        menu = self.get_object()
        if self.request.user == menu.author:
            return True
        return False
    

@login_required
def profile(request):
    context['page'] = 'profile'
    return render(request, 'businessdashboard/profile.html', context)

@login_required
def businesspage(request):
    context = {
        'menu-items': Menu.objects.all()
    }
    return render(request, 'businessdashboard/businesspage.html', context)


@login_required
def editbusinesspage(request):
    context = {
        'menu-items': Menu.objects.all()
    }
    return render(request, 'businessdashboard/editbusinesspage.html', context)

@login_required
def viewrating(request):
    context['page'] = 'viewrating'
    return render(request, 'businessdashboard/viewrating.html', context)