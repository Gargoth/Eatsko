from django.urls import path
from . import views
from .views import EateryListView
from .views import DashboardEateryListView
from .views import (
    ReviewListView,
    ReviewDetailView,
    ReviewCreateView,
    ReviewUpdateView,
    ReviewDeleteView
)

urlpatterns = [
    path('', DashboardEateryListView.as_view(), name='userdashboard-dashboard'),
    path('profile', views.profile, name='userdashboard-profile'),
    path('campusmap', views.campusmap, name='userdashboard-campusmap'),
    path('findeatery', EateryListView.as_view(), name='userdashboard-findeatery'),
    path('eaterypage', views.eaterypage, name='userdashboard-eaterypage'),
    path('viewrating', ReviewListView.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('review/new/', ReviewCreateView.as_view(), name='review-create'),
    path('review/<int:pk>/update/', ReviewUpdateView.as_view(), name='review-update'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),
    path('eaterypage/<int:eatery_id>', views.eaterypage, name='userdashboard-eaterypage'),

]
