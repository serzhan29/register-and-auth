from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    path('', views.index, name='index'),
    path('accounts/login/profile/', views.profile, name='profile'),
    path('register/accounts/profile/', views.profile, name='profile'),
]
