
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
import django.contrib.auth
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required

# Create your views here.

# home view
def home(request):
    return render(request, 'secondary/index.html')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f"Your message has been sent. Thank you {name}")
            form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'secondary/contact.html', context)

def about(request):
    return render(request, 'secondary/about.html')

@login_required(login_url='login-page')
@admin_only
def admin(request):
    students = Student.objects.all()
    total_students = students.count()
    staff = Staff.objects.all()
    total_staff = staff.count()
    subjects = Subject.objects.all()
    total_subjects = subjects.count()
    courses = Course.objects.all()
    total_courses = courses.count()


    context = {
        'students': students,
        'total_students': total_students,
        'total_staff': total_staff,
        'total_subjects': total_subjects,
        'total_courses': total_courses
    }
    return render(request, 'hod_template/home_content.html', context)


def student(request):
    return render(request, 'student_template/home_content.html')

@allowed_users(allowed_roles=['parent'])
def parents(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        group = user.groups.all()[0].name
        
        if group == 'parent':
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            return HttpResponse('You are not authorized to be here. Thank You!')
    
    return render(request, 'parent_template/parent_login.html')

def parentReg(request):
    form = ParentForm()

    if request.method == 'POST':
        form = ParentForm(request.POST)

        if form.is_valid():
            # form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            address = form.cleaned_data.get('address')
            country = form.cleaned_data.get('country')
            state = form.cleaned_data.get('state')
            gender = form.cleaned_data.get('gender')

            User = django.contrib.auth.get_user_model()
            user = User.objects.create_user(username=username, first_name = first_name, last_name=last_name, email=email, password='parent123')
            group = Group.objects.get(name='parent')
            user.groups.add(group)
            user.save()
            parent = Parent(first_name=first_name, middle_name=form.cleaned_data.get('middle_name'), last_name=last_name, username=username, email=email, address=address, country=country, gender=gender, state=state, user=user)
            parent.save()
            return redirect('parents')

    context = {
        'form': form
    }
    return render(request, 'parent_template/parent_registration.html', context)

@unauthorized_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        # loging in the user
        if user is not None:
            login(request, user)
            print('hello logged in')
            if request.user.groups.all()[0].name == 'admin':
                return redirect('principal')
            return redirect('home')
        else:
            print('not logged in')
    return render(request, 'main_app/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login-page')
