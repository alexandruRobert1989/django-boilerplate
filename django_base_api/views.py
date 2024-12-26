from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def page_one(request):
    return render(request, 'page_one.html')


def page_two(request):
    return render(request, 'page_two.html')
