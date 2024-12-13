from django.core.validators import (
    RegexValidator, 
    MinLengthValidator, 
    EmailValidator, 
    MaxLengthValidator
)
from django.core.exceptions import ValidationError
import re
class Validacao:
    def validate_cnpj(self,value):
        # Remover caracteres não numéricos
        cnpj = re.sub(r'\D', '', value)
        
        # Verificar se tem 14 dígitos
        if len(cnpj) != 14:
            raise ValidationError('CNPJ deve ter 14 dígitos.')
        
        # Validação do dígito verificador (algoritmo básico)
        def calc_digito_verificador(self,cnpj, peso):
            soma = sum(int(digito) * p for digito, p in zip(cnpj, peso))
            resto = soma % 11
            return 0 if resto < 2 else 11 - resto

        # Pesos para o primeiro dígito verificador
        peso1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        # Pesos para o segundo dígito verificador
        peso2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        # Calcular dígitos verificadores
        digito1 = calc_digito_verificador(cnpj[:12], peso1)
        digito2 = calc_digito_verificador(cnpj[:13], peso2)

        # Verificar se os dígitos verificadores estão corretos
        if int(cnpj[12]) != digito1 or int(cnpj[13]) != digito2:
            raise ValidationError('CNPJ inválido.')

    def validate_cep(self,value):
        # Remover caracteres não numéricos
        cep = re.sub(r'\D', '', value)
        
        # Verificar se tem 8 dígitos
        if len(cep) != 8:
            raise ValidationError('CEP deve ter 8 dígitos.')

    def validate_telefone(self,value):
        # Remover caracteres não numéricos
        telefone = re.sub(r'\D', '', value)
        
        # Verificar se tem entre 10 e 11 dígitos (DDD + telefone)
        if len(telefone) < 10 or len(telefone) > 11:
            raise ValidationError('Telefone inválido. Deve ter 10 ou 11 dígitos.')