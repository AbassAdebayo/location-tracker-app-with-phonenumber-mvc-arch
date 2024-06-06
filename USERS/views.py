from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from USERS.forms import CustomUserCreationForm
from USERS.forms import LoginForm


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('track')
        
    else:
        form = CustomUserCreationForm()
    return render(request,  'USERS/TEMPLATES/USERS/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('track')
            else:
                form.add_error(None, 'Invalid username or password')
                
    else:
        form  = LoginForm()
    return render(request,  'USERS/TEMPLATES/USERS/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
            