from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.registerUser, name='signup'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('home/', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('add/', views.addBlog, name='add_blog'),
    path('user_profile/', views.userProfile, name='user_profile'),
    path('user_profile/<slug:slug>/delete', views.deleteBlog, name='delete_blog'),
    path('user_profile/<slug:slug>/update', views.updateBlog, name='update_blog'),
    path('<slug:slug>/', views.detail, name='post_detail'),
    path('<slug:slug>/like', views.likeCount, name='like_count')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)