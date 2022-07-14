from django.shortcuts import render
from django.utils import timezone
from .models import Post
import boto3
import os 

def read_latest(request):
    client = boto3.client('dynamodb',
                        region_name='us-east-2',
                        aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
                        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"))
    db = boto3.resource('dynamodb', 
                        region_name='us-east-2',
                        aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
                        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))   

    table = db.Table('temps')
    response = table.scan()
    items = response['Items']
    items = sorted(items, reverse=True, key=lambda x: x['timestamp'])
    return render(request, 'blog/read_latest.html', { 'item': items[0] } )

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def render_template(request): 
    return render(request, 'blog/index.html')

