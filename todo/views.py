from django.shortcuts import render

def home_page(request):
    return render(request, 'todo/home.html')

def about_page(request):
    return render(request, 'todo/about.html')