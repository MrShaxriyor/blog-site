from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.






def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Notugri username yoki parol')
            return redirect('get-login')
        
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('get-home')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, "Passwords notugro")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username mavjud")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Successfully")
        return redirect('home')

    return render(request, 'accounts/reg.html')


@login_required
def home_view(request):
    return render(request, 'accounts/home.html')