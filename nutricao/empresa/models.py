from django.db import models
from core.validadorts import Validacao
from django.core.validators import (
    RegexValidator, 
    MinLengthValidator, 
    EmailValidator, 
    MaxLengthValidator
)
from django.core.exceptions import ValidationError
import re


class Empresa(models.Model):
        
        CHOICES_CNAE = [("refeições","5611-2/01 - restaurantes e similares"),
                        ("bebidas","5611-2/02 - bares e outros estabelecimentos especializados  em   servir bebidas"),
                        ("lanches","5611-2/03- lanchonetes, casas de chá, de sucos e similares")]
        

        CHOICES_NUMEROS_REFEICOES = [("100","até 100"),
                                     ("101 A 300","101 a 300"),
                                     ("301 A 1000","301 a 1000"),
                                     ("1001 A 2500","1001 a 2500"),
                                     ("mais de 2500","acima de 2500")]
        

        CHOICES_NUMEROS_FUNCIONARIOS = [("1 A 4","de 1 a 4"),
                                        ("5 A 9","5 a 9"),
                                        ("10 A 19","10 a 19"),
                                        ("mais de 20","20 ou mais")]
        
        CHOICES_TEM_RESPONSAVEL = [("SIM","sim"),
                                   ("NAO","não")]

        CHOICES_FORMACAO = [("CA","Curso de Capacitação"),
                            ("NT","Nível Técnico"),
                            ("NS","Nível Superior")]
        
        CHOICES_ALVARA = [("SIM","sim"),
                          ("NÃO","NÃO"),
                          ("EP","em processo"),
                          ("NA","não se aplica")]
        
        classificacao = models.CharField(max_length=100, default='Não Possui Avaliação')

        razao_social = models.CharField(
                "razão social: ", 
                max_length=100,
                validators=[
                MinLengthValidator(3, 'Razão social deve ter no mínimo 3 caracteres'),
                MaxLengthValidator(100, 'Razão social deve ter no máximo 100 caracteres')
                ]
        )
        
        nome_fantasia = models.CharField(
                "Nome Fantasia: ", 
                max_length=100,
                validators=[
                MinLengthValidator(3, 'Nome fantasia deve ter no mínimo 3 caracteres'),
                MaxLengthValidator(100, 'Nome fantasia deve ter no máximo 100 caracteres')
                ]
        )
        
        
        
        inscricao = models.CharField(
                "Inscrição Estadual / Municipal ",
                max_length=20,
                validators=[
                RegexValidator(
                        r'^[A-Za-z0-9]+$', 
                        'Inscrição deve conter apenas letras e números'
                )
                ]
        )
        
        cnpj = models.CharField(
                "CNPJ/CPF ",
                unique=True,
                max_length=14,
                validators=[Validacao.validate_cnpj]
        )
        
        fone = models.CharField(
                "Fone: ",
                max_length=20,
                validators=[Validacao.validate_telefone]
        )
        
        email = models.CharField(
                "E-MAIL: ",
                unique=True, 
                max_length=100,
                validators=[EmailValidator(message='E-mail inválido')]
        )
        
        endereco = models.CharField(
                "Endereço(Rua/Av): ",
                max_length=100,
                validators=[
                MinLengthValidator(3, 'Endereço deve ter no mínimo 3 caracteres'),
                MaxLengthValidator(100, 'Endereço deve ter no máximo 100 caracteres')
                ]
        )
        
        complemento = models.CharField(
                "Complemento: ",
                max_length=50,
                blank=True,  # Opcional
                null=True
        )
        
        bairro = models.CharField(
                "Bairro: ",
                max_length=50,
                validators=[
                MinLengthValidator(3, 'Bairro deve ter no mínimo 3 caracteres'),
                MaxLengthValidator(50, 'Bairro deve ter no máximo 50 caracteres')
                ]
        )
        
        municipio = models.CharField(
                "Município: ",
                max_length=50,
                validators=[
                MinLengthValidator(3, 'Município deve ter no mínimo 3 caracteres'),
                MaxLengthValidator(50, 'Município deve ter no máximo 50 caracteres')
                ]
        )
        
        uf = models.CharField(
                "-UF: ",
                max_length=2,
                validators=[
                RegexValidator(
                        r'^[A-Z]{2}$', 
                        'UF deve conter duas letras maiúsculas'
                )
                ]
        )
        
        cep = models.CharField(
                "CEP: ",
                max_length=8,
                validators=[Validacao.validate_cep]
        ) 
        
        razao_social = models.CharField("razão social: ",max_length=100,blank=False)
        nome_fantasia = models.CharField("Nome Fantasia: ",max_length=100,blank=False)
        inscricao = models.CharField("Inscrição Estadual / Municipal ",max_length=20,blank=False)
        cnpj = models.CharField("CNPJ ",unique= True,max_length=14,blank=False)
        fone = models.CharField("Fone: ",max_length=20,blank=False)
        email = models.CharField("E-MAIL: ",unique= True, max_length=100,blank=False)
        endereco = models.CharField("Endereço(Rua/Av): ",max_length=100,blank=False)
        complemento = models.CharField("Complemento: ",max_length=50,blank=False)
        bairro = models.CharField("Bairro: ",max_length=50,blank=False)
        municipio = models.CharField("Município: ",max_length=50,blank=False)
        uf = models.CharField("-UF: ",max_length=2,blank=False)
        cep = models.CharField("CEP: ",max_length=8,blank=False)
        cnae = models.CharField("Classificação Nacional da Atividade Econômica (CNAE)",max_length=10,choices=CHOICES_CNAE,default="",blank=False)
        numero_de_refeicoes = models.CharField("Número de refeições servidas diariamente",max_length=12,choices=CHOICES_NUMEROS_REFEICOES,default="",blank=False)
        numero_funcionarios = models.CharField("Pessoal ocupado (número de pessoas envolvidas nesta atividade econômica/ n° funcionários):",blank=False,max_length=10,choices=CHOICES_NUMEROS_FUNCIONARIOS,default="")
        tem_responsavel = models.CharField("Tem responsável pelas Boas Práticas?",max_length=10,choices=CHOICES_TEM_RESPONSAVEL,default="",blank=False)
        formacao_academica = models.CharField("Formação Acadêmica",max_length=10,choices=CHOICES_FORMACAO,default="",blank=False)
        responsavel_legal = models.CharField("Responsável Legal/ Responsável legal do Estabelecimento:",max_length=100,blank=False)
        redes_sociais = models.CharField("Possui Redes sociais? ",max_length=100,blank=True)
        site = models.CharField("link do site se possuir",max_length=100,blank=True)
       


