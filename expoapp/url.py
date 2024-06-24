from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
     path('', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('passwordreset/', views.reset_password, name='reset_password'),
    path('tab/',views.tab,name='viewtab'),
    path('base/',views.base)
    
]