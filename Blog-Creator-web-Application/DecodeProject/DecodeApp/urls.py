from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


#define route path to redirect one to another pages

urlpatterns = [
    path('', views.Home,name="Home"),
    
    path('login/', views.login,name="login"),
    
    path('loged/', views.loged,name="loged"),
   
    path('blog/',views.blog, name="blog"),
    
    path('sendQuery/',views.sendQuery,name="sendQuery"),
    
    path('admin/', admin.site.urls,name="admin"),
    
    path('readPost/<int:id>',views.readPost,name="readPost"),
    
    path('About/',views.About,name="About"),
    
    path('Searching/',views.Searching, name="Searching"),
   
    
   ]
