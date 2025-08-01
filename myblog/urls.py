"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="blog"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("login",views.login,name="login"),
    path('services',views.services,name="services"),
    path('logout', views.logout, name="logout"),
    path('blog',views.blog,name='blog'),
    path("createblog",views.createblog,name="createblog"),
    path('post/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('registration',views.registration,name='registration'),
    path('search',views.search, name='search' ),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

