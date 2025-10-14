from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.forms import UserChangeForm



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
        fields = ['nome', 'email', 'cpf', 'tipo_usuario', 'password1', 'password2']

        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        # Personaliza os labels dos campos se necessário
        self.fields['nome'].label = 'Nome Completo'
        self.fields['email'].label = 'E-mail'
        self.fields['cpf'].label = 'CPF'
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirme a Senha'
        if not (user and user.is_staff):  # ou user.is_superuser
            self.fields.pop('tipo_usuario')
        
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

class CustomUserChangeForm(UserChangeForm):
    
    # É uma boa prática definir as opções como um atributo de classe
    TIPOS_USUARIO = [
        ("VIGILANCIA", "Vigilância"),
        ("PREFEITURA", "Prefeitura"),
        ("ADM", "Administrador"),
        ("OUTRO", "Outro")
    ]
    
    # Defina o campo aqui para poder referenciá-lo facilmente
    tipo_usuario = forms.ChoiceField(
        choices=TIPOS_USUARIO,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        # Remova 'password', pois não é seguro editá-lo diretamente aqui.
        # Use PasswordChangeForm para isso.
        fields = ['nome', 'email', "cpf", "tipo_usuario"]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None) 
        
        super().__init__(*args, **kwargs)
        
        # Agora, a lógica para remover o campo
        if self.user and self.user.tipo_usuario != 'ADM':
            # Use 'tipo_usuario' (singular), que é o nome correto do campo
            del self.fields['tipo_usuario']
    