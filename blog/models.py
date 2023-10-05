from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
# from django.contrib.auth import get_user_model

# Create your models here.

# User = get_user_model()

# class Author(models.Model):
#     name = models.OneToOneField(User, on_delete=models.CASCADE)
#     prof_pic = models.ImageField()

#     def __str__(self):
#         return self.name.username

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, password=password)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username=username, email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    # password = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['email']

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.title
    
    verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(default='blog_details')
    overview = models.TextField()
    content =models.TextField()
    author = models.ForeignKey('blog.User', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True, default='uploads/default_blog.png')
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()

    def __str__(self):
        return self.title
    
    
class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
