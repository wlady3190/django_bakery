from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Comment
# Create your views here.

class CreateBlogView(CreateView):
    model = Comment
    template_name = 'blog/comment_new.html'
    fields = ['profession', 'content']
    