from django.shortcuts import render,redirect
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
def Welcome(request):
    return render(request, 'index.html')
# def Login(request):
#     return render(request, 'auth/login.html')
def ChatbotInterface(request):
    return render(request, 'chatbot.html')
def about(request):
    return render(request, 'about.html')
from django.shortcuts import render


def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
           login(request, user)
           return redirect('chatbot')
        else:
           messages.success(request,('There was an error loggin in .Try again'))
           return render(request, 'auth/login.html')
    else:
           return render(request,'auth/login.html')
