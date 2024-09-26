from django.db import models
from django.contrib.auth.models import AbstractUser

# from django.contrib.auth import get_user_model                # get a instance model from User model in django.contrib.auth
# User = get_user_model()

# AbstractUser  its have many field whene we want to create a model and add custom field      
# AbstractBaseUser its did not any fields similar to AbstractUser and we should define all fields we need

# after create model please tell django project in settings file AUTH_USER_MODEL = 'users.CustomUser'
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, verbose_name="تلفن همراه")
    email_active_code = models.CharField(max_length=100, verbose_name="کد فعال سازی ایمیل")

    # show CustomUser models name in django admin panel
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.get_full_name()
    

