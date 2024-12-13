from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User



class RegisterAdminForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['nome', 'email', 'cpf', 'tipo_usuario', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personaliza os labels dos campos se necessário
        self.fields['nome'].label = 'Nome Completo'
        self.fields['email'].label = 'E-mail'
        self.fields['cpf'].label = 'CPF'
        self.fields['tipo_usuario'].label = 'Tipo de Usuário'
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirme a Senha'
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este e-mail já está em uso.')
        return email
        
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if User.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError('Este CPF já está cadastrado.')
        return cpf



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['nome', 'email', 'cpf', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personaliza os labels dos campos se necessário
        self.fields['nome'].label = 'Nome Completo'
        self.fields['email'].label = 'E-mail'
        self.fields['cpf'].label = 'CPF'
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirme a Senha'
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este e-mail já está em uso.')
        return email
        
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if User.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError('Este CPF já está cadastrado.')
        return cpf



class LoginForm(forms.Form):
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu e-mail'})
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Sua senha'})
    )