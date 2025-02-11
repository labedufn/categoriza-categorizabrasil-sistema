from django import forms
from django.db import models
from .models import Empresa





class FormularioEmpresa(forms.ModelForm):
    
    class Meta:
        model = Empresa
        fields = ["razao_social","nome_fantasia","inscricao",
                  "cnpj","fone","email","cep","endereco","complemento",
                  "bairro","municipio","uf","cnae","numero_de_refeicoes",
                  "numero_funcionarios","tem_responsavel","formacao_academica",
                  "responsavel_legal","redes_sociais","site"
                  ]
        