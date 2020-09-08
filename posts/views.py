from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.

def post_list(request):
    object_list = Post.objects.all()
    return render(request,'index.html',{'objects':object_list})

def create_post(request):
    content = 'create'
    return render(request,'index.html',{'content':content})
    
def post_details(request,details):
    object_details = get_object_or_404(Post,title = details)
    content = 'details'
    return render(request,'details.html',{'object':object_details,'content':content})
    
def post_update(request):
    content = 'update'
    return render(request,'index.html',{'content':content})
    
def post_delete(request):
    content = 'delete'
    return render(request,'index.html',{'content':content})
    