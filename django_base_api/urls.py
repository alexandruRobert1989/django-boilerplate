from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views  # Import this line

from . import views
from .views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Root URL pointing to the home_view
    path('page-one/', views.page_one, name='page_one'),
    path('page-two/', views.page_two, name='page-two'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('user/', views.user, name='user_page'),
    path('staffuser/', views.staffuser, name='staffuser_page'),  # Add this line




]
