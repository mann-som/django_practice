from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Mann',
        'title': 'django',
        'date': '9 aug 2024'
    },
    {
        'author': 'Mann2',
        'title': 'django2',
        'date': '10 aug 2024'
    },
    {
        'author': 'Mann3',
        'title': 'django3',
        'date': '11 aug 2024'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog_app/home.html', context)

def about(request):
    return render(request, 'blog_app/about.html', {'title':'second page'})
