from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.ShowLoginPage, name='ShowLoginPage'),
    path('doLogin', views.doLogin, name='DoLogin'),
    path('Logout_user', views.Logout_user, name='Logout_user'),
    path('get_user_details', views.GetUserDetails, name='GetUserDetails'),
]