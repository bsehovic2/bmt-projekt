# articles/views.py
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "home.html"


class PostDetailView(LoginRequiredMixin, DetailView):  # new
    model = Post
    template_name = 'post.html'


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # new
    model = Post
    fields = ('title', 'body')
    template_name = 'post_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin, DeleteView):  # new
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ('title', 'body')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)