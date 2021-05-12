from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone

# def index(request):
#     #name = "Michael"
#     nums = [1, 2, 3, 4, 5]
#     return render(request, 'index.html', {"my_list" : nums})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'homepage/post_list.html', {'posts': posts})