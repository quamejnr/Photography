from django.urls import path
from photo.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='post-home'),
    path('new_post/', PostCreateView.as_view(), name='post-create'),
    path('post/<str:slug>', PostDetailView.as_view(), name='post-detail'),
    path('post/<str:slug>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<str:slug>/delete', PostDeleteView.as_view(), name='post-delete'),

]
