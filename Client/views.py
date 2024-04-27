from django.shortcuts import render

def Welcome(request):
    return render(request, 'index.html')
def Login(request):
    return render(request, 'login.html')