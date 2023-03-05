from django.urls import path
from . import views

urlpatterns = [
    path('', views.opensession, name='sessionmanager-opensession'),
    path('loginuser/', views.loginuser, name='sessionmanager-loginuser'),
    path('loginbusinessowner/', views.loginbusinessowner, name='sessionmanager-loginbusinessowner'),
    path('signup/', views.signup, name='sessionmanager-signup'),
]

