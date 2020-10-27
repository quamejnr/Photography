from django.urls import path
from photo.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='post-home'),
    path('new_post/', PostCreateView.as_view(), name='post-create'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-post'),
    path('post/<str:slug>', PostDetailView.as_view(), name='post-detail'),
    path('post/<str:slug>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<str:slug>/delete', PostDeleteView.as_view(), name='post-delete'),

]
