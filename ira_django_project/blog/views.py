from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
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
    paginate_by = 5  # no. posts per page


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        """get the user associated with the username (get from url)
        if user does not exist, return 404 page does not exist"""
        user = get_object_or_404(User, username=self.kwargs.get('username'))  # get username from the parameter in the url
        # we are overriding the query the list view is making, we are overriding ['-date_posted'] above -- move below like so
        return Post.objects.filter(author=user).order_by('-date_posted')  # limit posts on page to this filter

        


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

