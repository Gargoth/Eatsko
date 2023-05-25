from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='sessionmanager/login.html'), name='sessionmanager-opensession'),
    path('loginredirect/', views.loginredirect, name='sessionmanager-loginredirect'),
    path('logout/', auth_views.LogoutView.as_view(template_name='sessionmanager/logout.html'), name='sessionmanager-logout'),
    path('signup/', views.signup, name='sessionmanager-signup'),
    path('postsignupbusinessowner/', views.postsignup_businessowner, name='sessionmanager-postsignupbusinessowner'),
]
