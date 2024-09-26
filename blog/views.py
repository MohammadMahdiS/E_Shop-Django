from datetime import date
from django.shortcuts import render

all_latest_posts = [
    {
        'slug': 'learning-django',
        'title': 'how to learn django',
        'author': 'Mohammad Mahdi Soleimani',
        'image': 'django.png',
        'date': date(2024, 4, 3),
        'short_description': 'django is most popular python framework in the world of programming for create web development, Machine learning and AI',
        'text': """we in this course first learn introduction of python programming and have practice to confident learning after we start
                django framework from introduction such as virtual-machine, startproject, startapp, django file explorer, settings file,
                djanog models, views, urls and panel admin."""

    },
    {
        'slug': 'Master-Django-Rest-introduction',
        'title': ' Master Django Rest introduction',
        'author': 'Mohammad Mahdi Soleimani',
        'image': 'master.jpg',
        'date': date(2024, 8, 5),
        'short_description': 'django rest is the best solution for handle API base application for backend and client base apps',
        'text': """ Rest API is the important section for programmer who want to work with other api base apps and other client
        language programming such as React, Angular for develop advanced web application or scintific api apps """
    },
    {
        'slug': 'Machine-Learning-Data-Science',
        'title': 'Machine Learning Data Science',
        'author': 'Mohammad Mahdi Soleimani',
        'image': 'ml.png',
        'date': date(2024, 9, 11),
        'short_description': 'ML mean Machine Learning for analyse and prediction data',
        'text': """Machine Learning with web base network and gather data of client is analyse data is most popular field in last years
                we start learning course with cleaning data, split data, divide undefined data in columns and analyse data and show it 
                with charts and prediction with machine"""
    },
     {
        'slug': 'Learning-ML-Step-by-Step',
        'title': 'Learning ML Step-by-Step',
        'author': 'Mohammad Mahdi Soleimani',
        'image': 'python.png',
        'date': date(2024, 9, 11),
        'short_description': 'ML mean Machine Learning for analyse and prediction data',
        'text': """Machine Learning with web base network and gather data of client is analyse data is most popular field in last years
                we start learning course with cleaning data, split data, divide undefined data in columns and analyse data and show it 
                with charts and prediction with machine"""
    }
    
]

def get_date(post):
    return post['date']

def blog(request):
    sorted_posts = sorted(all_latest_posts, key=get_date)
    latest_posts = sorted_posts[:-2] 
    context = {
        'latest_posts': latest_posts
    }
    return render(request, 'blog/blog.html', context)

def posts(request):
    context = {
        'all_posts': all_latest_posts
    }
    return render(request, 'blog/all-posts.html', context)

def single_post(request, slug):
    
    retrive_post = next((post for post in all_latest_posts if post['slug'] == slug), None)

    context = {
        'post' : retrive_post
    }
    return render(request, 'blog/post-detail.html', context)