# myapp/authentication/urls.py

from django.urls import path
from .views import register, home, login_view, logout_view

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home, name='home'),
]