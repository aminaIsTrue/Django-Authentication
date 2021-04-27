from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns= [

    path ('',views.home, name = 'home-path'),
    path ('register/',views.register_view, name = 'register-path'),
    # path ('login/',views.login_view, name = 'login-path'),
    #path ('logout/',views.logout_view, name = 'logout-path'),



    # registration with CBVs

    path ('login/',auth_views.LoginView.as_view(template_name= "users/login.html"), name = 'login-path'),
    path ('logout/',auth_views.LogoutView.as_view(template_name= "users/logout.html"), name = 'logout-path'),




]