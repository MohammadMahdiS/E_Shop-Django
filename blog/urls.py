from django.urls import path
from .views import blog, posts, single_post
urlpatterns = [
    path('', blog, name="blog-page"),
    path('posts/', posts, name="post-page" ),
    path('posts/<slug:slug>', single_post, name="post-detail-page"),            # website.com/posts/second-post

]