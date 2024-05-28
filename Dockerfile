# Utilizando uma imagem base do Python 3.9
FROM python:3.9-slim

# Instalar ferramentas de rede e compilador
RUN apt-get update && apt-get install -y \
    net-tools \
    iproute2 \
    gcc \
    python3-dev

# Definindo o diretório de trabalho no container
WORKDIR /app

# Copiando os arquivos de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiando todos os arquivos do projeto para o diretório de trabalho
COPY . .

# Executando o script de captura de pacotes e depois o de análise
CMD ["sh", "-c", "python capture_packets.py $INTERFACE && python analyze_traffic.py"]