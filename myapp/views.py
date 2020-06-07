from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import  CreateUserForm
from .forms import PostForm

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
				return redirect('login')
		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')
		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def home(request):
	library = Library.objects.all()
	return render(request, 'accounts/dashboard.html',{'library':library})

@login_required(login_url='login')
def review(request,pk):
	post_list=Post.objects.all()
	library_id=pk
	current_user = request.user
	context={'library_id':library_id,'current_user':current_user,'post_list':post_list}
	return render(request, 'accounts/review.html',context)

@login_required(login_url='login')
def submit_post(request):
	if request.method == 'POST':
		data = PostForm(request.POST)
		if data.is_valid():
			title = data.cleaned_data['title']
			content = data.cleaned_data['content']
			lib = data.cleaned_data['library']
			author = request.user
			library = Library.objects.get(id=lib)
			value = Post(title=title,content=content,author=author,library= library)
			value.save()
			messages.success(request, 'comment submitted ')
			return redirect('home')
	
			