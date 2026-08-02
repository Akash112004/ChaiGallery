from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request, 'index.html')

def categories(request):
    return render(request, 'index.html')

def upload(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'index.html')