from .models import User, Post, Category
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm


# class UserSignUp(ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#         widgets = {'password' : forms.PasswordInput()}


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # Specify the User model
        fields = ('username', 'email', 'password1', 'password2')  # Fields to include in the form


class UserLogIn(forms.Form):
    username = forms.CharField(max_length=20, label='Username')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')


class AddBlog(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'overview', 'content', 'thumbnail', 'categories', 'featured']

    author = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False)
    thumbnail = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'custom-file-input'}), required=False)