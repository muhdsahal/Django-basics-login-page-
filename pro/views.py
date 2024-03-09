
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout  
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib import messages




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Enter a valid Username and Password')   
    return render(request, 'login.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='user_login')
def home(request):
    return render(request,'home.html')
    
@login_required(login_url='user_login')
def logout_user(request):
    logout(request )
    return redirect('user_login')