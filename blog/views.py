from django.shortcuts import render
from django.utils import timezone
from .models import Post
import boto3
import os 

def read_latest(request):
    url = 'https://jx7a1ot8db.execute-api.us-east-2.amazonaws.com/GetMostRecent'
    response = urlopen(url)
    data_json = json.loads(response.read())
    item = data_json['body']                                                                                                      
    return render(request, 'blog/read_latest.html', { 'item': item } )

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def render_template(request): 
    return render(request, 'blog/index.html')

