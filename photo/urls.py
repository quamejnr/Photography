from django.urls import path
from photo.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, \
                        PhotographerPostListView, \
                        PhotographerListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='post-home'),
    path('new_post/', PostCreateView.as_view(), name='post-create'),
    path('photographer/', PhotographerListView.as_view(), name='photographer'),
    path('photographer/<str:username>', PhotographerPostListView.as_view(), name='photographer-post'),
    path('post/<str:slug>', PostDetailView.as_view(), name='post-detail'),
    path('post/<str:slug>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<str:slug>/delete', PostDeleteView.as_view(), name='post-delete'),

]
