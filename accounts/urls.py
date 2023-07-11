from django.urls import path
from . import views


urlpatterns = [
    path('', views.login),
    path('signup/', views.sign_up),
    path('confirm/', views.confirming),
    path('reset/', views.password_reset),
    path('keep/', views.save_reset),
]
