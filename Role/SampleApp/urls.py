from django.urls import path
from SampleApp import views
from django.contrib.auth import views as v

urlpatterns = [
	path('',views.home,name='home'),
	path('about/',views.about,name='about'),
	path('contact/',views.contact,name='contact'),
	path('register/',views.register,name='register'),
	path('dashboard/',views.dashboard,name='dashboard'),
	path('login/',v.LoginView.as_view(template_name='html/login.html'),name='login')
	
]