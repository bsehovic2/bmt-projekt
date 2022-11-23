# articles/views.py
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "home.html"


class PostDetailView(DetailView):  # new
    model = Post
    template_name = 'post.html'


class PostUpdateView(UpdateView):  # new
    model = Post
    fields = ('title', 'body',)
    template_name = 'post_edit.html'


class PostDeleteView(DeleteView):  # new
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ('title', 'body', 'author')