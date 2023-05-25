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
from django.contrib import messages
from userdashboard.models import Menu
from businessdashboard.forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import user_passes_test

# Helper Functions


def is_owner(user):
    return user.groups.filter(name="businessowner").exists()


owner_required = user_passes_test(is_owner)

# View Functions
context = {}


@owner_required
def dashboard(request):
    context = {
        'menu': request.user.user_profile.eatery.menuitems.all()
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
    template_name = 'businessdashboard/menu_form.html'
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


@owner_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.user_profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('businessdashboard-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.user_profile)

    context['page'] = 'profile'
    context['u_form'] = u_form
    context['p_form'] = p_form

    return render(request, 'businessdashboard/profile.html', context)


@owner_required
def businesspage(request):
    context = {
        'menu-items': request.user.user_profile.eatery.menuitems.all(),
    }
    return render(request, 'businessdashboard/businesspage.html', context)


@owner_required
def editbusinesspage(request):
    context = {
        'menu-items': request.user.user_profile.eatery.menuitems.all(),
    }
    return render(request, 'businessdashboard/editbusinesspage.html', context)


@owner_required
def viewrating(request):
    context['page'] = 'viewrating'
    return render(request, 'businessdashboard/viewrating.html', context)
