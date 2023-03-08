from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.opensession, name='sessionmanager-opensession'),
    path('loginuser/', auth_views.LoginView.as_view(template_name='sessionmanager/loginuser.html'), name='sessionmanager-loginuser'),
    path('loginbusinessowner/', auth_views.LoginView.as_view(template_name='sessionmanager/loginbusinessowner.html'), name='sessionmanager-loginbusinessowner'),
    path('signup/', views.signup, name='sessionmanager-signup'),
    path('logout/', auth_views.LoginView.as_view(template_name='sessionmanager/logout.html'), name='sessionmanager-logout'),
]

