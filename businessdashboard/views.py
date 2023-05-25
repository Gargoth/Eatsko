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
from userdashboard.models import Menu, Eatery, Review
from businessdashboard.forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Avg

# Helper Functions


def is_owner(user):
    return user.groups.filter(name="businessowner").exists()


owner_required = user_passes_test(is_owner)

# View Functions
context = {}


@owner_required
def dashboard(request):
    eatery = Eatery.objects.get(id=request.user.user_profile.eatery.id)  # Replace <eatery_id> with the ID of the current eatery
    reviews = Review.objects.filter(eatery=eatery)
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    context = {
        'menu': request.user.user_profile.eatery.menuitems.all(),
        'eatery': eatery,
        'reviews': reviews,
        'average_rating': average_rating
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
    template_name = 'businessdashboard/menu_detail.html'
    context_object_name = 'menu'


class MenuCreateView(LoginRequiredMixin, CreateView):
    model = Menu
    template_name = 'businessdashboard/menu_form.html'
    fields = ['title', 'content', 'price']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.eatery = self.request.user.user_profile.eatery
        return super().form_valid(form)


class MenuUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Menu
    template_name = 'businessdashboard/menu_form.html'
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
    template_name = 'businessdashboard/menu_confirm_delete.html'
    success_url = '/business/businesspage'

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
    return render(request, 'businessdashboard/businesspage.html')


@owner_required
def editbusinesspage(request):
    return render(request, 'businessdashboard/editbusinesspage.html')


@owner_required
def viewrating(request):
    eatery = Eatery.objects.get(id=request.user.user_profile.eatery.id)  # Replace <eatery_id> with the ID of the current eatery
    reviews = Review.objects.filter(eatery=eatery)
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']

    context = {
        'eatery': eatery,
        'reviews': reviews,
        'average_rating': average_rating,
        'range_five': [1, 2, 3, 4, 5],
        'page': 'viewrating'
    }

    return render(request, 'businessdashboard/viewrating.html', context)
