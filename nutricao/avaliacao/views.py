from django.shortcuts import render,get_object_or_404, redirect
from .forms import FormularioAvaliacao
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Formulario
from empresa.models import Empresa
def filtrarDict(item_inicial,item_final,input_dict):
    
    return dict(list(input_dict.items())[item_inicial:item_final+1])
#def verifica_eliminacao(dict):
    
def soma_dict(dict, valor_questoes):
    total_pontuacao = 0
    contador = 0
    
    for resposta in dict.items():
        if resposta[1] == 'IN':
            questao = resposta[0]
            idx = int(questao[7:])
            total_pontuacao += valor_questoes[idx-1]
        contador+=1
    return total_pontuacao

def verifica_eliminacao(respostas,variavel_controle):
    
    for resposta in respostas.items():
            if resposta[1] == 'IN':
                if variavel_controle == False:
                    variavel_controle = True
                else:
                     variavel_controle = False
    
    
            
    return variavel_controle
def calcular_pontuacao(valor_questoes,respostas):
    eliminado = False
    classificado = True
    respostas_eliminatorias = filtrarDict(0,2,respostas)
    respostas_Abastecimento = filtrarDict(3,6,respostas)
    respostas_Estrutura = filtrarDict(7,8,respostas)
    respostas_Higienizacao = filtrarDict(9,14,respostas)
    respostas_Controle = filtrarDict(15,17,respostas)
    respostas_Manipuladores = filtrarDict(18,20,respostas)
    respostas_Materias_primas = filtrarDict(21,27,respostas)
    respostas_Preparo_alimento = filtrarDict(28,39,respostas)
    respostas_Armazenamento = filtrarDict(40,48,respostas)
    respostas_classificatorias = filtrarDict(49,50,respostas)
    lista_somas = [
        soma_dict(respostas_Preparo_alimento,valor_questoes),
        soma_dict(respostas_Armazenamento,valor_questoes),
        soma_dict(respostas_Abastecimento,valor_questoes),
        soma_dict(respostas_Estrutura,valor_questoes),
        soma_dict(respostas_Higienizacao,valor_questoes),
        soma_dict(respostas_Controle,valor_questoes),
        soma_dict(respostas_Manipuladores,valor_questoes),
        soma_dict(respostas_Materias_primas,valor_questoes),
        
    ]
    eliminado = verifica_eliminacao(respostas_eliminatorias,eliminado)
    classificado = verifica_eliminacao(respostas_classificatorias,classificado)

    return [sum(lista_somas),eliminado,classificado], lista_somas                    
def salvar_pontuacoes(lista_somas,form):
        form.pt_abastecimento_agua = lista_somas[0]
        form.pt_estrutura = lista_somas[1]
        form.pt_higienizacao = lista_somas[2]
        form.pt_controle_integrado  = lista_somas[3]
        form.pt_manipuladores = lista_somas[4]
        form.pt_materias_primas = lista_somas[5]
        form.pt_preparo_alimento = lista_somas[6]
        form.pt_armazenamento = lista_somas[7]
        return form
def classificar_pontuacao(form):
        valor_questoes = ["eliminatorio","eliminatorio","eliminatorio",1,1,2,1,12,2,12,12,3,6,3,3,2,4,2,3,9,3,6,2,2,4,8,16,2,12,9,8,12,8,12,16,12,12,12,6,16,8,8,12,8,12,16,6,6,4,"classificatorio","classificatorio"]
        respostas = form.cleaned_data
        respostas = {chave: valor for chave, valor in respostas.items() if not chave.endswith("_descricao")}
        pontuacoes,lista_somas = calcular_pontuacao(valor_questoes,respostas)
                    
        if int(pontuacoes[0])>=156 or pontuacoes[1]== True or pontuacoes[2]== False:
                classificacao = "PENDENTE"
        elif int(pontuacoes[0])>=69:
            classificacao = "C"
        elif int(pontuacoes[0])>=3:
            classificacao = "B"
        else:
            classificacao = "A"
        print("teste3: ",str(pontuacoes[0]))
        return str(pontuacoes[0]), classificacao,lista_somas
@login_required(login_url="/login")
def avaliacao_update(request,formulario_existente,empresa):
    if request.method == 'POST':
        form = FormularioAvaliacao(request.POST, instance=formulario_existente)
        if form.is_valid():
            
            formulario = form.save(commit=False)
            formulario.Usuario = request.user
            formulario.total_pontuacao, empresa.classificacao,lista_somas = classificar_pontuacao(form)
            formulario = salvar_pontuacoes(lista_somas,formulario)
            if request.user.tipo_usuario == "VIGILANCIA":
                empresa.save()
                formulario.save()
            print("teste: ",formulario.total_pontuacao)
            return render(request, "relatorio.html",{'form': formulario,'questoes_valor': formulario.valor_questoes,'questoes_texto':formulario.lista_requisitos})
    else:
        form = FormularioAvaliacao(instance=formulario_existente)
    
    return render(request, 'avaliacao.html', {'form': form})

@login_required(login_url="/login")
def avaliacao_create(request,empresa):
    if request.method == 'POST':
        form = FormularioAvaliacao(request.POST)
        if form.is_valid():
            formulario = form.save(commit=False)
            formulario.Empresa = empresa
            formulario.Usuario = request.user
            formulario.total_pontuacao, empresa.classificacao,lista_somas = classificar_pontuacao(form)
            formulario = salvar_pontuacoes(lista_somas,formulario)
            if request.user.tipo_usuario == "VIGILANCIA":
                empresa.save()
                formulario.save()
            formulario.save(commit = False)
            return render(request, "relatorio.html",{'form': formulario,'questoes_valor': formulario.valor_questoes,'questoes_texto':formulario.lista_requisitos})
            
                 
    else:
        form = FormularioAvaliacao()
    
    return render(request, "avaliacao.html", {'form': form})

@login_required(login_url="/login")
def avaliacao(request, id):
    empresa = get_object_or_404(Empresa, id=id)
    try:
        formulario_existente = Formulario.objects.get(Empresa=empresa)
        return avaliacao_update(request=request, formulario_existente=formulario_existente,empresa=empresa)
    except Formulario.DoesNotExist:
        return avaliacao_create(request=request,empresa=empresa)
        

    

@login_required(login_url="/login")
def relatorio(request, id):
    form = Formulario()   
 
    
    empresa = get_object_or_404(Empresa, id=id) 
    try:
        formulario_existente = Formulario.objects.get(Empresa=empresa)
        return render(request, "relatorio.html",{'form': formulario_existente,'questoes_valor': form.valor_questoes,'questoes_texto':form.lista_requisitos})
        
    except Formulario.DoesNotExist:
        return redirect("empresa")

    