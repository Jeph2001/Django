from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Board, Topic, Post
# from .forms import NewTopicForm
from .forms import TopicForm, BoardForm, PostForm


# Create your views here.
def landing(request):
    return render(request, 'landing_page.html')


def confirming(request):
    return render(request, 'confirmation.html')



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
            return HttpResponseRedirect('/web_app/confirm/')
    
    else:
        form = TopicForm()
    
    return render(request, 'create_topic.html', {'form': form})


def get_board(request):
    if request.method == 'POST':
        formm = BoardForm(request.POST)
        if formm.is_valid():
            formm.save()
            return HttpResponseRedirect('/web_app/confirm/')
    else:
        formm = BoardForm()
    return render(request, 'admin_data.html', {'formm': formm})


def get_post(request):
    if request.method == 'POST':
        pform = PostForm(request.POST)
        if pform.is_valid:
            pform.save()
            return HttpResponseRedirect('/web_app/confirm/')
    else:
        pform = PostForm()
    return render(request, 'create_post.html', {'pform': pform})








