from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate

def index(request):
    #Condicionais de autenticação
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return HttpResponse('<h1>LOGADO(A)</h1>')
            else:
                return HttpResponse('<h1>USUÁRIO OU SENHA INVÁLIDO(S)</h1>')

    credenciais = LoginForm()
    context = {
        'form':credenciais,
    }
    return render(request,'home/login.html',context)