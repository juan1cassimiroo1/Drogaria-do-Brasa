FROM python:3.12-slim

WORKDIR /app

# Instala dependências do sistema necessárias para o Python
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de dependências primeiro (otimiza o cache do Docker)
COPY requirements.txt .

# Instala as bibliotecas do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Define o comando padrão que será executado ao iniciar o container
ENTRYPOINT ["python", "-m", "src.main"]