from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'secondary/index.html')


# login function
def userLogin(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		print(user)

		if user is not None:
			login(request, user)
			return redirect('home')

	return render(request, 'secondary/login.html')

def logout(request):
	logout(request)
	return redirect('login')