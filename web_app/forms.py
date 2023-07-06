from django import forms
from .models import Board, Topic, Post

# class NewTopicForm(forms.ModelForm):
#     message = forms.CharField(widget=forms.Textarea(), max_length=4000)

#     class Meta:
#         model = Topic
#         fields = ['subject', 'message']


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = "__all__"


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = "__all__"


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"




