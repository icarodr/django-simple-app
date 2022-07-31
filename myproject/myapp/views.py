from django.shortcuts import render
from .forms import LoginForm

def index(request):
    return render(request,'diario/login.html')