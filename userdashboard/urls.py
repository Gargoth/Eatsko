from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='userdashboard-dashboard'),
    path('profile', views.profile, name='userdashboard-profile'),
    path('campusmap', views.campusmap, name='userdashboard-campusmap'),
    path('findeatery', views.findeatery, name='userdashboard-findeatery'),
]
