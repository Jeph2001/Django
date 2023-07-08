from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.sign_up),
    path('confirm/', views.confirming),
    path('login/', views.login),
]
