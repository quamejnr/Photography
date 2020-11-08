from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from user.models import Profile
from django.contrib.auth.models import User


class PostListView(ListView):
    model = Post
    ordering = ['-date_posted']
    paginate_by = 5


class PhotographerPostListView(ListView):
    model = Post
    paginate_by = 6
    template_name = 'photo/portfolio.html'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(photographer=user).order_by('-date_posted')

    def get_context_data(self, **kwargs):
        # retrieves profile data of a photographer
        context = super().get_context_data(**kwargs)
        photographer = get_object_or_404(User, username=self.kwargs.get('username'))
        context['profile'] = Profile.objects.get(user=photographer)
        return context


class PhotographerListView(ListView):
    model = Profile
    paginate_by = 5
    template_name = 'photo/photographer.html'


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
    template_name = 'photo/post_update_form.html'

    def test_func(self):
        # Ensures users can only edit their respective posts
        post = self.get_object()
        if self.request.user == post.photographer:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    def test_func(self):
        # Ensures users can only delete their respective posts
        post = self.get_object()
        if self.request.user == post.photographer:
            return True
        return False

    def get_success_url(self):
        # Reversing success url to photographer's portfolio instead of home
        username = self.object.photographer
        return reverse_lazy('photographer-post', kwargs={'username': username})
