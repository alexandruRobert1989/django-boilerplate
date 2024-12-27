from django.contrib.auth import logout
from django.shortcuts import render, redirect

def home_view(request):
    # Render the home page without redundant `is_user_group` calculation
    return render(request, 'home.html')

def page_one(request):
    return render(request, 'page_one.html')

def page_two(request):
    return render(request, 'page_two.html')

def login_redirect_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to the home page
    return render(request, 'login.html')

def custom_logout(request):
    logout(request)  # Logs out the user
    return redirect('home')  # Redirect to the home page

def user(request):
    return render(request, 'user.html')
