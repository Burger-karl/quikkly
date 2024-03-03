from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterUserForm
from .models import User

# Create your views here.

def register_sender(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_sender = True
            var.save()
            messages.success(request, 'Account created, Please log in to continue')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('register-sender')
    else:
        form = RegisterUserForm()
        context = {'form':form}
        return render(request, 'user/register_sender.html', context)


def register_rider(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_rider = True
            var.save()
            messages.success(request, 'Account created for rider')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('register-rider')
    else:
        form = RegisterUserForm()
        context = {'form':form}
        return render(request, 'user/register_rider.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, f'You are logged in as {user}')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'user/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'Session ended. Please, login to continue')
    return redirect('login')