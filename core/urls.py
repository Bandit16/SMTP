
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.homepage, name='home'),
    path('settings/', views.accountSettings, name='setting'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('explore/', views.explore, name='explore'),


]
