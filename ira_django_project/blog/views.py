from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    # we need to create a var called model
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'  # i.e. posts == context key in our home func
    ordering = ['-date_posted']  # goes oldest to newest -- add a '-' in front to reverse this order


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    # override the form valid method
    
    def form_valid(self, form):
        # set author of form before submission
        form.instance.author = self.request.user
        # validate form by running the form_valid method on our parent class
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    # override the form valid method
    
    def form_valid(self, form):
        # set author of form before submission
        form.instance.author = self.request.user
        # validate form by running the form_valid method on our parent class
        return super().form_valid(form)

    def test_func(self):
        """UserPassesTestMixin will run this to check for correct
        conditions, i.e. correct author"""
        post = self.get_object()  # get post we are currently trying to update
        # check current user is author of post
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        """UserPassesTestMixin will run this to check for correct
        conditions, i.e. correct author"""
        post = self.get_object()  # get post we are currently trying to update
        # check current user is author of post
        if self.request.user == post.author:
            return True
        return False



def about(request):
    title = {'title': 'About'}
    return render(request, 'blog/about.html', title)

