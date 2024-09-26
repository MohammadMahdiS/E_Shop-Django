from django.db import models

# Blog Models

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField()
    short_description = models.CharField(max_length=255)


    def __str__(self):
        return self.title