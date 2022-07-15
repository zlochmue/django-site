from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_template, name='render_template'),
    path('posts/', views.post_list, name='post_list'),
    path('sensor/', views.read_latest, name='read_latest'),
]

