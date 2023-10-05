from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.registerUser, name='signup'),
    path('login/', views.loginUser, name='login'),
    path('home/', views.home, name='home'),
    path('add/', views.addBlog, name='add_blog'),
    path('user_profile/', views.userProfile, name='user_profile'),
    path('user_profile/<slug:slug>/delete', views.deleteBlog, name='delete_blog'),
    path('<slug:slug>/', views.detail, name='post_detail')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)