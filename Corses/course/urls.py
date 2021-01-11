from django.urls import path
from course import views
from django.contrib.auth import views as v


urlpatterns = [
    path('', views.home, name='home'),
    path('course/', views.course, name='course'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', v.LoginView.as_view(template_name='mycourse/login.html'), name='login'),
    path('logout/', v.LogoutView.as_view(template_name='mycourse/logout.html'), name='logout'),
    path('addcourse/',views.addcourse,name='addcourse'),
    path('mycourses/',views.mycourses,name='mycourses'),
    path('profile/',views.profile,name='profile'),
    path('update/',views.update_user,name='update_user'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('upload/',views.upload_course_content,name='upload_course_content'),
    path('Content',views.Content,name='Content')
    

]
