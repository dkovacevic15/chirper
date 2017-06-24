from django.shortcuts import render
from django.contrib.auth import authenticate, get_user_model, login, logout
# Create your views here.

def register_view(request):
    return render(request, 'form.html', {})
    
def login_view(request):
    return render(request, 'form.html', {})

def logout_view(request):
    return render(request, 'form.html', {})