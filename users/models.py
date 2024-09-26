# from django.db import models
# from django.contrib.auth import User

# class CustomUser(models.Model):
#     first_name = models.CharField(max_length=255, blank=True)
#     last_name = models.CharField(max_length=255, blank=True)
#     email = models.EmailField(blank=True)
#     password = models.CharField(max_length=255)
#     is_staff = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=True)
#     last_login = models.DateField(blank=True)
#     is_authenticated = models.BooleanField(default=True)


# class CustomUserManager(models.Model):
#     def create_user(username, email=None, password=None, **extra_fields):
#         user = User.get_object()
#         return user
    
#     def create_superuser(username, email=None, password=None, **extra_fields):
#         superuser = User.get_queryset()
#         return superuser
