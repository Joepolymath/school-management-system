from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import *
from django.contrib.auth.decorators import login_required

# Create your views here.

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