from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from .models import *
from .forms import *

def home(request):
    context = {'blogs' : BlogModel.objects.all()}
    return render(request , 'home.html' , context)

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password = password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.error(request,"Invalid Details")
            return render(request,"login.html")
    else:
        return render(request,"login.html")
    
def logout(request):
    auth.logout(request)
    return redirect("login")

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['emailid']
        try:
            if User.objects.filter(username = username).exists():
                print(User.objects.filter(username = username))
                messages.error(request,"User name is already taken")
                return redirect("register")
            user = User.objects.create_user(username=username,password = password,email = email,first_name = first_name,last_name = last_name)
            user.save()
            return render(request,"login.html")
        except:
            messages.error(request,"Problem")
            return render(request,"register.html")
    else:
        return render(request,"register.html")

def add_blogs(request):
    context = {'form' : BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user
            
            if form.is_valid():
                content = form.cleaned_data['content']
            
            blog_obj = BlogModel.objects.create(
                user = user , title = title, 
                content = content, image = image
            )

            return redirect('add_blogs')
    except Exception as e :
        pass
    
    return render(request , 'add_blogs.html' , context)

def my_blogs(request):
    d = BlogModel.objects.filter(user = request.user)
    #print(d.blog_id)
    return render(request,"my_blogs.html",{'message' : d})

def blog_delete(request , id):
    try:
        blog_obj = BlogModel.objects.get(blog_id = id)
        
        if blog_obj.user == request.user:
            blog_obj.delete()
        
    except Exception as e:
        pass

    return redirect('my_blogs')

def update_blog(request,id):
    context = {}
    try:       
        blog_obj = BlogModel.objects.get(blog_id = id)
        
        initial_dict = {'content': blog_obj.content}
        form = BlogForm(initial = initial_dict)
        if request.method == 'POST':
            form = BlogForm(request.POST)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user
            print(image)
            blog_obj1 = BlogModel.objects.get(blog_id = id)
        
            if blog_obj1.user == request.user:
                blog_obj1.delete()

            if form.is_valid():
                content = form.cleaned_data['content']
            # print(content)

            blog_obj = BlogModel.objects.create(
                user = user , title = title, 
                content = content, image = image
            )    
        context['blog_obj'] = blog_obj
        context['form'] = form
    except Exception as e :
        pass
    return render(request , 'update_blog.html' , context)

def see_blogs(request,id):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(blog_id = id).first()
        context['blog_obj'] =  blog_obj
        # print(context)
    except Exception as e:
        pass
    return render(request , 'see_blogs.html' , context)

def my_profile(request):
    context = {"user":User.objects.all().filter(username = request.user)}
    return render(request,'my_profile.html',context)