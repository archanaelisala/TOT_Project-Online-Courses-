from django.urls import path
from Hsp import views
from django.contrib.auth import views as v

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', v.LoginView.as_view(template_name='hsp/login.html'), name='login'),
    path('logout/', v.LogoutView.as_view(template_name='hsp/logout.html'), name='logout'),
    path('addpatient/',views.AddPatient,name='AddPatient'),
    path('ViewAllPatientsList/',views.ViewAllPatientsList,name='ViewAllPatientsList')

]
