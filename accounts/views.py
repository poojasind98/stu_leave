from urllib import response
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        context = {'data' : request.POST}
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
   
        if not user:
            messages.add_message(request,messages.ERROR,"Invalid Credentials")
            return render(request,'accounts/login.html',context)
        
        login(request,user)
        messages.add_message(request,messages.SUCCESS,f'Welcome{user.username}')
        return redirect(reverse('home'))

    return render(request,'accounts/login.html')


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print("User Created")
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request,'accounts/register.html',{'form':form})

def logout_user(request):
    logout(request)
    messages.add_message(request,messages.SUCCESS,'Successfully logged out')
    return redirect(reverse('login'))