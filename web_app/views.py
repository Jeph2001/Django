from django.shortcuts import render
from .models import Board, Topic, Post


# Create your views here.
def home(request):
    return render(request, 'home.html')


def board_data(request):
    saved = Board.objects.all()
    return render(request, 'admin_data.html', {'saved': saved})


def topic_data(request):
    topics = Topic.objects.all()
    return render(request, 'board_topic.html', {'topics':topics})


def post_data(request):
    posts = Post.objects.all()
    return render(request, 'post_data.html', {'posts':posts})





