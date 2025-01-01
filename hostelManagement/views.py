from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime
from django.db.models import Min, Max
from decimal import Decimal
from django.utils import timezone

# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request,"index.html")

def logout(request):
    logout(request)
    return redirect('signin')  # Redirects to the signin page after logout

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        # Check if the username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different username.')
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists. Please use a different email.')
            return redirect('signup')

        # Create a new user and hash the password
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        # Create admin record (ensure Admin model is used correctly)
        admin = Admin.objects.create(  # Using 'Admin' here
            user=user,
            phone=phone,
        )
        admin.save()

        messages.success(request, 'Welcome! Signup Successful.')
        return redirect('signin')  # Ensure you're redirecting to the right URL

    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = authenticate(request, username=username, password=password)
        print(f"Authentication result: {user_obj}")  # Debugging line

        if user_obj:
            login(request, user_obj)
            print(f"User logged in: {user_obj.username}")  # Debugging line
            return redirect('home')
        else:
            print("Login failed.")  # Debugging line

    return render(request, 'signin.html')

def view_students(request):
    students = Student.objects.all()
    return render(request, 'view_students.html', {'students': students})

def view_staff(request):
    staff_data = HostelStaff.objects.all()  # Fetch all staff data
    return render(request, 'view_staff.html', {'staff_data': staff_data})