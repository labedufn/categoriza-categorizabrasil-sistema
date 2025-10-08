#!/usr/bin/env bash

# 1. Espera pelo Banco de Dados
# O hostname 'db' é o nome do serviço no docker-compose.yml, porta 5432

# 2. Coletar Arquivos Estáticos
# Isso escreve no volume 'static_data'
python manage.py collectstatic --noinput

# 3. Aplicar Migrações
python manage.py migrate --noinput

# 4. Iniciar Gunicorn (Servidor WSGI)
exec gunicorn --bind 0.0.0.0:8000 nutricao.wsgi:application