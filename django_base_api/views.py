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
    # Fetch the logged-in user's group(s)
    user_groups = request.user.groups.values_list('name', flat=True) if request.user.is_authenticated else []

    # Prepare the context with user details
    context = {
        'username': request.user.username,
        'email': request.user.email,
        'first_name': request.user.first_name or "N/A",
        'last_name': request.user.last_name or "N/A",
        'roles': ', '.join(user_groups) if user_groups else "No roles",
        'last_login': request.user.last_login,
    }
    return render(request, 'user.html', context)

# View for the Staff User page
def staffuser(request):
    return render(request, 'staffuser.html')
