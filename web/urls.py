from django.urls import path, include
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/login/profile/', views.profile, name='profile'),
    path('register/accounts/profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),  # URL для выхода
    path('change_password/', views.change_password, name='change_password'),  # URL для смены пароля
]

