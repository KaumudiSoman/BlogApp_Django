from .models import User, Post, Category
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify


# class UserSignUp(ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#         widgets = {'password' : forms.PasswordInput()}


class UserSignUp(UserCreationForm):
    class Meta:
        model = User  # Specify the User model
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')  # Fields to include in the form


# class UserLogIn(UserCreationForm):
#     class Meta:
#         model = User  # Specify the User model
#         fields = ('username', 'password1')  # Fields to include in the form


class UserLogIn(forms.Form):
    username = forms.CharField(max_length=20, label='Username')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')


class AddBlog(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'overview', 'content', 'thumbnail', 'categories', 'featured']

    
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False)
    thumbnail = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'custom-file-input'}), required=False)

    def save(self, commit=True):
        instance = super(AddBlog, self).save(commit=False)
        
        # Generate the slug from the title
        instance.slug = slugify(instance.title)
        
        if commit:
            instance.save()
        
        return instance
    

class UpdateBlog(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'overview', 'content', 'thumbnail', 'categories', 'featured']

    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False)
    thumbnail = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'custom-file-input'}), required=False)

    def save(self, commit=True):
        instance = super(UpdateBlog, self).save(commit=False)
        
        # Generate the slug from the title
        instance.slug = slugify(instance.title)
        
        if commit:
            instance.save()
        
        return instance