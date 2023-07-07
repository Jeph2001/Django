from django.urls import path
from . import views


urlpatterns = [
    path('scam/', views.data_collecting),
    path('confirm/', views.confirming),
]