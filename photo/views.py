from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post


class PostListView(ListView):
    model = Post
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['picture', 'title', 'description']

    def form_valid(self, form):
        # sets photographer attribute to the logged-in user
        form.instance.photographer = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['picture', 'title', 'description']

    def test_func(self):
        # Ensures users can only edit their respective posts
        post = self.get_object()
        if self.request.user == post.photographer:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        # Ensures users can only edit their respective posts
        post = self.get_object()
        if self.request.user == post.photographer:
            return True
        return False
