from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin,Permission
from django.contrib.contenttypes.models import ContentType
# Primeiro criamos um Manager customizado
from django import forms
from django.contrib.auth.models import User



class CustomUserManager(BaseUserManager):
    def create_user(self, email, nome, cpf, tipo_usuario, password=None):
        if not email:
            raise ValueError('Usuários devem ter um email')
        
        user = self.model(
            email=self.normalize_email(email),
            nome=nome,
            cpf=cpf,
            tipo_usuario=tipo_usuario
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, cpf, tipo_usuario, password):
        user = self.create_user(
            email=email,
            nome=nome,
            cpf=cpf,
            tipo_usuario=tipo_usuario,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    TIPOS_USUARIO = [
        ("VIGILANCIA", "Vigilância"),
        ("PREFEITURA", "Prefeitura"),
        ("ADM", "Administrador"),
        ("OUTRO", "Outro")
    ]

    nome = models.CharField(max_length=100, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False, unique=True, db_index=True)
    tipo_usuario = models.CharField(choices=TIPOS_USUARIO, max_length=13, blank=False, null=False)
    email = models.EmailField('Email', max_length=100, unique=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'cpf', 'tipo_usuario']

    class Meta:
        ordering = ['-tipo_usuario', 'nome']
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'
        permissions = [
            ("pode_cadastrar","pode cadastrar outros usuarios"),
        ]

    def __str__(self):
        return f'{self.nome} - {self.email}'
    
    @property
    def inicializar_permissoes(self):
        if self.tipo_usuario == "Vigilancia":
            user_content_type = ContentType.objects.get_for_model(User)
            permissoes_usuarios = Permission.objects.filter(
                ntent_type=user_content_type,
                codename__in=[
                    'pode_cadastrar', 
                ]
            )
            self.user_permissions.add(*permissoes_usuarios)




