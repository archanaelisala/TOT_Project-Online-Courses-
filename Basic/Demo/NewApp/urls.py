from django.urls import path
from NewApp import views
from django.contrib.auth import views as v

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', v.LoginView.as_view(template_name='NewApp/login.html'), name='login'),
    path('logout/', v.LogoutView.as_view(template_name='NewApp/logout.html'), name='logout'),

]
