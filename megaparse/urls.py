from django.contrib import admin
from django.urls import path

from . import views
from .views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Root URL pointing to the home_view
    path('page-one/', views.page_one, name='page_one'),
    path('page-two/', views.page_two, name='page-two')
]
