from django.shortcuts import render, redirect, get_object_or_404

from django.conf import settings 
from django.conf.urls.static import static 

from .models import Post

from django.views.generic import (ListView, DetailView,
)

from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'home.html', context)

class PostListView(ListView): 
    model = Post 
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['?']

class PostDetailView(DetailView):
    model = Post

def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        title = Post.objects.filter(title__contains = search)
        date_posted = Post.objects.filter(date_posted__contains = search)
        return render(request, 'search.html', {'search':search, 'title':title,'date_posted':date_posted})
    else:
        return render(request, 'search.html')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful.")
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")