from django.shortcuts import render
from . import models

def hello_world(request):
    return render(request, 'index.html')
def blog_all(request):
    post = models.Post.objects.all()
    return render(request, 'post_list.html', {'post_list': post})
