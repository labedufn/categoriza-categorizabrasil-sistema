from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from .models import User
from .form import RegisterAdminForm, RegisterForm, CustomUserChangeForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import FormView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from .form import LoginForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserChangeForm

class PrefeituraAdmAccessMixin(UserPassesTestMixin):
    def test_func(self):
        # Verifica se o usuário tem permissão
        return self.request.user.is_authenticated and \
               self.request.user.tipo_usuario in ['PREFEITURA', 'ADM']
    
    def handle_no_permission(self):
        # Redireciona para uma página de acesso negado ou login
        return redirect('home')

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'usuario/usuario_list.html'
    context_object_name = 'usuarios'
    login_url = '/login'  
    
    def get_queryset(self):
        if (not self.request.user.tipo_usuario == 'ADM'):
            qs = User.objects.filter(is_active=True).exclude(tipo_usuario = 'ADM').order_by('-tipo_usuario', 'nome')
        else:
            qs = User.objects.filter(is_active=True).order_by('-tipo_usuario', 'nome')
        return qs


class UserAdminRegisterView(PrefeituraAdmAccessMixin,CreateView):
    model = User
    form_class = RegisterAdminForm
    template_name = 'usuario/cadastro.html'
    
    def get_success_url(self):
        return reverse('empresa')  # Certifique-se de que 'empresa' existe nas suas URLs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo_usuario'] = self.request.user.tipo_usuario
        return context
    
    def form_valid(self, form):
        # Salva o usuário
        user = form.save(commit=False)
        # Defina a senha de forma segura
        password = form.cleaned_data.get('password1')
        if password:
            user.set_password(password)
        user.save()
        
        # Faz login do usuário
        #login(self.request, user)
        
        return redirect(self.get_success_url())

class UserRegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'usuario/cadastro.html'
    
    def get_success_url(self):
        return reverse('empresa')  # Certifique-se de que 'empresa' existe nas suas URLs
    
    def form_valid(self, form):
        
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        if password:
            user.set_password(password)
            user.tipo_usuario = "OUTRO"
        user.save()
        
        # Faz login do usuário
        login(self.request, user)
        
        return redirect(self.get_success_url())
    
    

class CustomLoginView(FormView):
    template_name = 'usuario/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')  # Altere para sua página inicial após login
    
    def dispatch(self, request, *args, **kwargs):
        # Redireciona usuários já logados
        if request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
       
        user = authenticate(self.request, username=email, password=password)
        print("teste3   ", user)
        if user is not None:
            login(self.request, user)
            messages.success(self.request, f'Bem-vindo, {user.nome}!')
            return super().form_valid(form)
        else:
            messages.error(self.request, 'E-mail ou senha inválidos.')
            print("teste    ",email)
            print(password)
            return self.form_invalid(form)

class CustomLogoutView(LogoutView):
    next_page = 'login'  # Nome da URL para redirecionamento após logout
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(request, 'Você saiu com sucesso!')
        return super().dispatch(request, *args, **kwargs)


@login_required(login_url="/login")
def usuario_update(request, id):
    user = get_object_or_404(User, pk=id)
    if request.user.tipo_usuario == "ADM":
        if request.method == "POST":
            form = CustomUserChangeForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Usuário atualizado com sucesso!')
                return redirect('home')
        else:
            form = CustomUserChangeForm(instance=user)
        
        return render(request, "usuario_update.html", {'form': form, 'user': user})
    else:
        return redirect("home")

    

@login_required(login_url="/login")
def usuario_delete(request, id):
    # Busca o usuário existente ou retorna 404
    user = get_object_or_404(User, pk=id)
    if request.user.tipo_usuario == "ADM":
        if request.method == "POST":
            # Confirma a exclusão
            user.delete()
            messages.success(request, 'Usuário excluído com sucesso!')
            return redirect('home')
        
        # Renderiza a página de confirmação de exclusão
        return render(request, "user_delete.html", {'user': user})
    else:
        return redirect("home")


def logout_view(request):
    logout(request)
    return redirect('cadastro')


