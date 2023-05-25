from django.urls import path
from . import views
from .views import EateryListView
from .views import DashboardEateryListView


urlpatterns = [
    path('', DashboardEateryListView.as_view(), name='userdashboard-dashboard'),
    path('profile', views.profile, name='userdashboard-profile'),
    path('campusmap', views.campusmap, name='userdashboard-campusmap'),
    path('findeatery', EateryListView.as_view(), name='userdashboard-findeatery'),
    path('eaterypage/<int:eatery_id>', views.eaterypage, name='userdashboard-eaterypage'),
]
