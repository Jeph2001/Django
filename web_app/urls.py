from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('admindata/', views.board_data),
    path('board/', views.topic_data),
    path('post/', views.post_data),
]