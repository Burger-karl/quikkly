from django.urls import path
from . import views

urlpatterns = [
    path('register-sender/', views.register_sender, name='register-sender'),
    path('register-rider/', views.register_rider, name='register-rider'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]