from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Eatery, Review, Profile
from userdashboard.forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Avg


# Helper Functions


def is_visitor(user):
    return user.groups.filter(name="visitor").exists()


visitor_required = user_passes_test(is_visitor)

# View Functions
context = {}


@visitor_required
def dashboard(request):
    context['page'] = 'dashboard'
    return render(request, 'userdashboard/dashboard.html', context)


@visitor_required
def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
                request.POST, request.FILES, instance=request.user.user_profile
                )

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('userdashboard-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.user_profile)

    context['page'] = 'profile'
    context['u_form'] = u_form
    context['p_form'] = p_form

    return render(request, 'userdashboard/profile.html', context)


@visitor_required
def campusmap(request):
    context['page'] = 'campusmap'
    return render(request, 'userdashboard/campusmap.html', context)


@visitor_required
def findeatery(request):
    context['page'] = 'findeatery'
    return render(request, 'userdashboard/findeatery.html', context)


@visitor_required
def eaterypage(request, eatery_id):
    context['page'] = 'eaterypage'
    context['eatery'] = Eatery.objects.get(id=eatery_id)
    return render(request, 'userdashboard/eaterypage.html', context)


@visitor_required
def eaterypagereviews(request, eatery_id):
    context['page'] = 'eaterypage'
    context['eatery'] = Eatery.objects.get(id=eatery_id)
    context['reviews'] = Review.objects.filter(eatery=context['eatery'])
    context['average_rating'] = context['reviews'].aggregate(Avg('rating'))['rating__avg']
    context['range_five'] = [1, 2, 3, 4, 5]

    return render(request, 'userdashboard/eaterypagereviews.html', context)


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


class DashboardEateryListView(ListView):
    model = Eatery
    template_name = 'userdashboard/dashboard.html'
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

class ReviewListView(ListView):
    model = Review
    template_name = 'userdashboard/review-list.html'
    ordering = ['-date_posted']

class ReviewDetailView(DetailView):
    model = Review

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'userdashboard/review_form.html'
    fields = ['rating', 'comment', 'eatery']

    success_url = '/user/'
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.profile = self.request.user.user_profile
        return super().form_valid(form)
    
class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['rating', 'comment', 'eatery', 'profile']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
            return True
        return False

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = '/'

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
            return True
        return False
