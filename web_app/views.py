from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Board, Topic, Post
# from .forms import NewTopicForm
from .forms import TopicForm, BoardForm


# Create your views here.
def home(request):
    return render(request, 'home.html')


# def board_data(request):
#     saved = Board.objects.all()
#     return render(request, 'admin_data.html', {'saved': saved})


def topic_data(request):
    topics = Topic.objects.all()
    return render(request, 'board_topic.html', {'topics':topics})


def post_data(request):
    posts = Post.objects.all()
    return render(request, 'post_data.html', {'posts':posts})


# def post_form(request):
#     return render(request, 'post_form.html')


# def create_topic(request):
#     if request.method == 'POST':
#         form = NewTopicForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return 'Yess!!'
#         else:
#             form = NewTopicForm()
        
#     return render(request, 'create_topic.html')


def get_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/web_app/post/')
    
    else:
        form = TopicForm()
    
    return render(request, 'create_topic.html', {'form': form})


def get_board(request):
    if request.method == 'POST':
        formm = BoardForm(request.POST)
        if formm.is_valid():
            formm.save()
            return HttpResponseRedirect('/web_app/post/')
    else:
        formm = BoardForm()
    return render(request, 'admin_data.html', {'formm': formm})





