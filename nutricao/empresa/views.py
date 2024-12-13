from .forms import FormularioEmpresa
from .models import Empresa
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from utils.decorators import LoginRequiredMixin
from .models import Empresa
from django.contrib import messages

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