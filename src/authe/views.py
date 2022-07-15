from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout 
from .models import CustomUser
from .forms import UserRegistrationForm, UserLoginForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('music:home')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


def login_view(request):
    login_form = UserLoginForm()
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return render(request, 'reply.html', {'message':'you signed in'})
        return render(request, 'reply.html', {'message':'current user does not exist'})
    return render(request, 'login.html', {'login_form':login_form})


def logout_view(request):
    logout(request)
    return render(request, 'logout.html', {'message': 'You logged out'})



