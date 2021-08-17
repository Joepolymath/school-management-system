from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

# home view
@login_required(login_url='login')
def home(request):
    return render(request, 'secondary/index.html')


# login view

def userLogin(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)
			print(user)

			if user is not None:
				login(request, user)
				return redirect('home')

		return render(request, 'secondary/login.html')

# logout view
@login_required(login_url='login')
def userLogout(request):
	logout(request)
	return redirect('login')