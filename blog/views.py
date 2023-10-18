from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import Category, Post, User
from .forms import UserLogIn, AddBlog, UserSignUp, UpdateBlog
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def registerUser(request):
    if request.method == 'POST':
        form1 = UserSignUp(request.POST)

        if form1.is_valid():
            user = form1.save(commit=True)
            login(request, user)
            return redirect('home')

            # try:
            #     posts = Post.objects.all()
            #     return redirect('home')
            # except Exception as e :
            #     return HttpResponse(e)

    else:
        form1 = UserSignUp()
    return render(request, 'register.html', {'form1' : form1})


def loginUser(request):
    if request.method == 'POST':
        form2 = UserLogIn(request.POST)
        print(request.POST)

        if form2.is_valid():
            username = form2.cleaned_data['username']
            password = form2.cleaned_data['password']
            print(username)
            print(password)
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse('Invalid Username or Password') 

            # try:
            #     if(User.objects.filter(email = email_list)).exists():
            #         posts = Post.objects.all()
            #         return redirect('home')
            #     else:
            #         return HttpResponse('You are not a registered user. Please Sign Up to continue.')
            # except:
            #     return HttpResponse('error')
    else:
        form2 = UserLogIn()
    return render(request, 'login.html', {'form2' : form2})


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts' : posts})


def detail(request, slug):
    post = get_object_or_404(Post, slug = slug)
    return render(request, 'detail.html', {'post' : post})


def addBlog(request):
    if request.method == 'POST':
        form3 = AddBlog(request.POST, request.FILES)

        if form3.is_valid():
            form3.save()

            try:
                posts = Post.objects.all()
                return redirect('home')
            except:
                return HttpResponse('error')

    else:
        form3 = AddBlog()
    return render(request, 'addpost.html', {'form3' : form3})



def search(request):
    query = request.GET.get('query', '')

    related_posts = Post.objects.filter(title__icontains = query)

    return render(request, 'search.html', {'related_posts' : related_posts, 'query' : query})


@login_required
def userProfile(request):
    if request.user.is_authenticated:
        user = request.user
        blogs = Post.objects.filter(author=user)
        return render(request, 'userprofile.html', {'user': user, 'blogs': blogs})
    else:
        return redirect('signup')
    


def deleteBlog(request, slug):
    posts = Post.objects.filter(slug=slug)
    # post = get_object_or_404(Post, slug=slug)
    if posts.exists():
        post_to_delete = posts.first()
        print(request.user)
        print(post_to_delete.author)

    if request.user == post_to_delete.author:
        post_to_delete.delete()
        return redirect('user_profile')
        

    return HttpResponse('permission denied')


def updateBlog(request, slug):
    # posts = Post.objects.filter(slug=slug)
    posts = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        form4 = UpdateBlog(request.POST, instance=posts)

        if form4.is_valid():
            form4.save()
            return redirect('user_profile')
        

    else:
        form4 = UpdateBlog(instance=posts)

    return render(request, 'updateblog.html', {'form4' : form4})


def logoutUser(request):
    logout(request)
    return redirect('login')