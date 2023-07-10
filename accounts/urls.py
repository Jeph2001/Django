from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.sign_up),
    path('confirm/', views.confirming),
    path('login/', views.login),
    path('reset/', views.password_reset),
    path('keep/', views.save_reset),
]
