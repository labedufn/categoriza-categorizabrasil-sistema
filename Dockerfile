FROM python:3.11-slim
# Configurações de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Instalar dependências de sistema, incluindo netcat-openbsd (CORRIGIDO)
# Tudo agrupado em um único RUN usando '&&' para otimizar a imagem
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        build-essential \
        libpq-dev \
        netcat-openbsd \
    && rm -rf /var/lib/apt/lists/* # <--- LIMPEZA NO MESMO RUN

# Instalar dependências Python (incluindo gunicorn)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código do projeto
COPY . /app/

# Definir o script de ponto de entrada
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]