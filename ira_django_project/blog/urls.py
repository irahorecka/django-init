from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    #  our blog.urls will handle the home (i.e. /blog) and home/about (i.e. /blog/about) urls.
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-post'),  # username with string dtype and name it 'user-post'
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # pk = primary key, int is the type
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # default is <model>_form.html, i.e. post_form.html
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]