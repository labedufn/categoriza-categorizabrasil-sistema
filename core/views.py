from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from usuario.models import Usuario
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def login_view(request):
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Autentica o usuário
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redireciona o usuário para a página de destino após o login
                return redirect(reverse('empresa'))  # Altere 'empresa' para o nome da sua página principal
        else:
            form = AuthenticationForm()

        return render(request, 'usuario/login.html', {'form': form})
            
@login_required(login_url = "/login")
def home(request):
     usuarios = Usuario.objects.all()
     return render(request,"core/home.html",{"users":usuarios})