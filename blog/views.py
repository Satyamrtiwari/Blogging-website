from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from blog.models import Contact
from datetime import datetime
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")


def registration(request):
    if request.method =="POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_pass= request.POST.get("pass")
        
        if password != confirm_pass:
             messages.error(request,"Passwords do not match !!")
             return redirect("registration")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists !!")
            return redirect("registration")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists !!")
            return redirect("registration")

        else:
            my_user = User.objects.create_user(username,email,password)
            my_user.save() 
            auth_login(request, my_user)

            messages.success(request, "You have registered and logged in successfully!")
            return redirect('blog')

    return render(request, "registration.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        new_contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        new_contact.save()
        messages.success(request, "You Contacted us Successfully!!")
    return render(request, 'contact.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
         
        if user is not None:
            auth_login(request, user)
            # Redirect to blog page instead of about
            return redirect("/blog")  # or use redirect("/blog/") if using URL path
        else:
            return render(request, "login.html", {'error': 'Invalid username or password'})
    return render(request, "login.html")

def services(request):
    return render(request, "services.html")

def logout(request):
    auth_logout(request)
    # return render(request, "logout.html")
    return render(request,"index.html")



def search(request):
    return render (request,'search.html')
    # return HttpResponse("This is the search page")
    



from django.shortcuts import render
from .models import post

def blog(request):
    # return render(request, 'blog.html')
    posts = post.objects.all().order_by('-created_at')
    return render(request, 'blog.html', {'posts': posts})

from .models import post
from django.contrib import messages


@login_required
def createblog(request):
    error = None

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        author = request.user.username  # Don't take this from form, use logged-in user
        image = request.FILES.get("image")  # Optional

        if title and content and author:
            new_post = post(title=title, content=content, author=author)
            if image:
                new_post.image = image
            new_post.save()
            messages.success(request, "You posted successfully!")
            return redirect('createblog')
        else:
            error = "Please fill all fields."

    # ✅ Always fetch the logged-in user's posts for GET or after error
    user_posts = post.objects.filter(author=request.user.username).order_by('-created_at')

    return render(request, "createblog.html", {
        'posts': user_posts,
        'error': error
    })



def blog_detail(request, post_id):
    blog_post = get_object_or_404(post, id=post_id)
    return render(request, 'blog_detail.html', {'post': blog_post})


# # from django.shortcuts import render, get_object_or_404, redirect
# # from .models import post

# from django.shortcuts import get_object_or_404, render, redirect
# from .models import Post  # import your Post model

from .models import post  # or from .models import Post

def edit_post(request, post_id):
    # Use the model class, not the variable name
    blog_post = get_object_or_404(post, id=post_id)

    if request.method == 'POST':
        blog_post.title = request.POST.get('title')
        blog_post.content = request.POST.get('content')
        if 'image' in request.FILES:
            blog_post.image = request.FILES['image']
        blog_post.save()
        messages.success(request, "Edited successfully!")
        return redirect('createblog')

    return render(request, 'edit_post.html', {'post': blog_post})


@login_required
def delete_post(request, post_id):
    blog_post = get_object_or_404(post, id=post_id)
    
    # Ensure only the author can delete their own post
    if request.user.username == blog_post.author:
        blog_post.delete()
        messages.success(request, "Post deleted successfully!")
    else:
        messages.error(request, "You are not authorized to delete this post.")
    
    return redirect('createblog')
