from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('about', include('about.urls')),
    path('contact', include('contact.urls')),
    path('login', include('login.urls')),
    path('services', include('services.urls')),
    path('logout', include('logout.urls')),
    path('blog', include('blog.urls')),
    path('createblog', include('createblog.urls')),
    path('edit_post', include('edit_post.urls')),
    path('registration',include('registration.urls')),
    path('search',include('search.urls')),
    path("delete_post", include('delete_post.urls'))

]


