from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path('signup/' , views.signup_view ,name='signup'),
    path('login/' , auth_views.LoginView.as_view(template_name='tracker/login.html',next_page='/applications/') , name = 'login'),

    path('logout/' , auth_views.LogoutView.as_view() , name='logout'),


    path('applications/', views.application_list, name='application_list'),

   path('applications/add/', views.add_application, name='add_application'), 

   path('applications/<int:id>/edit/' ,views.edit_application,name='edit_application')
]

