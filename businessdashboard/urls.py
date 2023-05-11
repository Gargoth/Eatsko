from django.urls import path
from . import views
from .views import (
    MenuListView,
    EditMenuListView,
    MenuDetailView,
    MenuCreateView,
    MenuUpdateView,
    MenuDeleteView
)

urlpatterns = [
    path('', views.dashboard, name='businessdashboard-dashboard'),
    path('profile', views.profile, name='businessdashboard-profile'),
    #path('businesspage', views.businesspage, name='businessdashboard-businesspage'),
    path('editbusinesspage', EditMenuListView.as_view(), name='businessdashboard-editbusinesspage'),
    path('viewrating', views.viewrating, name='businessdashboard-viewrating'),
    path('businesspage', MenuListView.as_view(), name='businessdashboard-businesspage'),
    path('menu/<int:pk>/', MenuDetailView.as_view(), name='menu-detail'),
    path('menu/new/', MenuCreateView.as_view(), name='menu-create'),
    path('menu/<int:pk>/update/', MenuUpdateView.as_view(), name='menu-update'),
    path('menu/<int:pk>/delete/', MenuDeleteView.as_view(), name='menu-delete'),
]
