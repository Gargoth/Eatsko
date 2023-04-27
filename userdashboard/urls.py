from django.urls import path
from . import views
from .views import EateryListView


urlpatterns = [
    path('', views.dashboard, name='userdashboard-dashboard'),
    path('profile', views.profile, name='userdashboard-profile'),
    path('campusmap', views.campusmap, name='userdashboard-campusmap'),
    path('findeatery', EateryListView.as_view(), name='userdashboard-findeatery'),
]
