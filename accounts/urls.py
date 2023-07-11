from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.login),
    path('logout/', auth_views.LogoutView.as_view()),
    path('signup/', views.sign_up),
    path('confirm/', views.confirming),
    path('reset/', views.password_reset),
    path('keep/', views.save_reset),
]
