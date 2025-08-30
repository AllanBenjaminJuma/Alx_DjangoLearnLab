from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import RegisterView, LoginView, LogoutView 




urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]