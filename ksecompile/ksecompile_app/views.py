from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages
from  django.contrib.auth import login, logout

def index(request):
    '''Returns the home page'''
    return render(request=request, template_name='ksecompile_app/index.html')

def login_page(request):
    '''Returns the user's login page'''
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()

    context = {
        'form': form,
    }

    return render(request=request, template_name='ksecompile_app/login.html', context=context)

def logout_page(request):
    '''Returns the user's logout page'''
    logout(request)

    return redirect('login')

def register_page(request):
    '''Returns the user registration page'''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration completed successfully.')
            return redirect('login')
        else:
            messages.error(request, 'Registration error.')
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }
    
    return render(request=request, template_name='ksecompile_app/register.html', context=context)


