from django.shortcuts import render


posts = [
    {
        "author": 'IraH',
        "title": 'Blog Post 1',
        "content": 'First post content',
        "date_posted": 'April 14, 2020'  # usually a datetime obj
    },
    {
        "author": 'GeneH',
        "title": 'Blog Post 2',
        "content": 'Second post content',
        "date_posted": 'April 15, 2020'  # usually a datetime obj
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    title = {'title': 'About'}
    return render(request, 'blog/about.html', title)

