from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='businessdashboard-dashboard'),
    path('profile', views.profile, name='businessdashboard-profile'),
    path('businesspage', views.businesspage, name='businessdashboard-businesspage'),
    path('editbusinesspage', views.editbusinesspage, name='businessdashboard-editbusinesspage'),
    path('viewrating', views.viewrating, name='businessdashboard-viewrating'),
]
