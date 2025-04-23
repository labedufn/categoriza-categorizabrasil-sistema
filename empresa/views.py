from .forms import FormularioEmpresa
from .models import Empresa
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from utils.decorators import LoginRequiredMixin
from .models import Empresa
from django.contrib import messages
from avaliacao.models import Formulario
from django.db.models import Q

@login_required(login_url="/login")
def empresa_update(request, id):
    # Busca a empresa existente ou retorna 404
    empresa = get_object_or_404(Empresa, id=id)
    
    if request.method == "POST":
        # Passa a instância existente para o formulário
        form = FormularioEmpresa(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empresa atualizada com sucesso!')
            return redirect('empresa_list')  # Redireciona para a lista de empresas
    else:
        # Cria o formulário com a instância existente para edição
        form = FormularioEmpresa(instance=empresa)
    
    return render(request, "empresa_update.html", {'form': form, 'empresa': empresa})

@login_required(login_url="/login")
def empresa_delete(request, id):
    # Busca a empresa existente ou retorna 404
    empresa = get_object_or_404(Empresa, id=id)
    
    if request.method == "POST":
        # Confirma a exclusão
        empresa.delete()
        messages.success(request, 'Empresa excluída com sucesso!')
        return redirect('empresa_list')
    
    # Renderiza a página de confirmação de exclusão
    return render(request, "empresa_delete.html", {'empresa': empresa})

@login_required(login_url="/login")
def empresa(request):
    form = FormularioEmpresa()
    if request.method == "POST":
        form = FormularioEmpresa(request.POST)
        if form.is_valid():

            form.save(commit=True)
                          
                
            return redirect("empresa")
        else:
            return render(request, "empresa.html", {'form':form})
    else:
        form = FormularioEmpresa()
        return render(request, "empresa.html", {'form':form})

class EmpresaList(LoginRequiredMixin, ListView):
    model = Empresa
    template_name = 'empresa_list.html' 
    login_url = '/login' 
    context_object_name = 'empresas' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        empresas = context['empresas']  # Todas as empresas listadas
        formularios = {}  # Dicionário para armazenar os formulários por empresa

        for empresa in empresas:
            try:
                # Busca o formulário relacionado à empresa e ao usuário logado
                formulario_existente = Formulario.objects.get(Empresa=empresa, Usuario=self.request.user)
                formularios[empresa.id] = formulario_existente
            except Formulario.DoesNotExist:
                # Caso não exista um formulário, atribua `None` ou crie um formulário vazio
                formularios[empresa.id] = None

        # Adiciona o dicionário de formulários ao contexto
        context['formularios'] = formularios
        context['search_query'] = self.request.GET.get('q', '')
        return context
    

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Get search query from URL parameters
        search_query = self.request.GET.get('q')
        
        if search_query:
            # Search across multiple fields (nome, email, username, etc.)
            queryset = queryset.filter(
                Q(nome_fantasia__icontains=search_query) |
                Q(cnpj__icontains=search_query) |
                Q(bairro__icontains=search_query)
            )
        
        return queryset.order_by('-nome_fantasia', 'nome_fantasia')

    