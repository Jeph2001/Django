from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('admindata/', views.get_board),
    path('board/', views.topic_data),
    path('post/', views.post_data),
    path('create/', views.get_topic, name='get_topic'),
]
