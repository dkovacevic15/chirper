from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, AnonymousUser
from posts.models import Post
# Create your views here.
def homepage(request):
    if request.user.is_authenticated():
        return render(request, 'site/homepage.html', {'posts': list(Post.objects.all())})
    else:
        return redirect('landingpage')

def landingpage(request):
    if request.user.is_authenticated():
        return redirect('homepage')
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('homepage')
        else:
            form = UserCreationForm()
        return render(request, 'site/signup.html', {'form': form})