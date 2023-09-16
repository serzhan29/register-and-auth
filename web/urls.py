
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('profile', profile_view, name="profile"),
]
