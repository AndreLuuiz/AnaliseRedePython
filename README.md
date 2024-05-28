# Aplicação de Análise de Tráfego

Esta aplicação captura pacotes de uma interface de rede especificada e exibe estatísticas básicas sobre o tráfego capturado.

## Requisitos

- Python 3.9
- Docker
- WinPcap 4
- SQLite3

## Configuração

### Clonar o Repositório

1. Clone o repositório:

   ```sh
   git clone https://github.com/AndreLuuiz/AnaliseRedePython.git
   cd AnaliseRedePython
   ```

## Arquivos

```text
/path/to/your/project
│
├── analyze_traffic.py
├── capture_packets.py
├── db_connection.py
├── Dockerfile
├── main.py
├── README.md
└── requirements.txt
```

## Executando a aplicação

### Executando localmente

Se preferir executar a aplicação localmente sem Docker:

1. Instale as dependências:

    ```sh
    pip install -r requirements.txt
    ```

2. Execute o script:

   ```sh
   python main.py
   ```

3. Selecione a opção 1:

   ```sh
   Escolha o modo de execução da aplicação:
   1. Executar localmente
   2. Executar com Docker
   Digite 1 ou 2: 1
   ```

4. Selecione a sua interface de rede como requisitado.

    ```sh
    Interfaces de rede disponíveis:
   1. lo0
   2. en0
   Escolha uma interface de rede pelo número: 2
    ```

### Utilizando Docker

1. Execute o script:

    ```sh
    python main.py
    ```

    O comando acima executa o script de captura de pacotes seguido do script de análise. A saída mostrará estatísticas básicas sobre o tráfego capturado.


2. Selecione a opção 2:

    ```sh
    Escolha o modo de execução da aplicação:
   1. Executar localmente
   2. Executar com Docker
   Digite 1 ou 2: 2
   ```

   A interface de rede utilizada como padrão para a execução com docker é a eth0.


## Análise de Tráfego

O script de análise analyze_traffic.py lê o arquivo captured_packets.json gerado pelo script de captura e exibe as seguintes estatísticas:

 • Número total de pacotes capturados.

 • Número de pacotes por protocolo (TCP, UDP, etc.).

 • Top 5 endereços IP de origem com mais tráfego.

 • Top 5 endereços IP de destino com mais tráfego.

## Detalhes dos Scripts

analyze_traffic.py

- Processa o arquivo JSON gerado pelo script de captura e calcula estatísticas básicas sobre o tráfego capturado.

capture_packets.py

- Captura pacotes de rede e salva as informações necessárias em um arquivo JSON.

capture_packets.json

- Local de armazenamento dos pacotes capturados como um arquivo JSON.

db_connection.py

- Realiza as especificações e conexões do banco de dados.

Dockerfile

- Define a configuração do ambiente Docker, instalando as dependências necessárias e configurando a execução dos scripts.

requirements.txt

- Lista as dependências Python necessárias para a aplicação, incluindo a biblioteca Scapy.

main.py

- Centraliza os comandos principais de execução.
- De acordo com o SO (Linux/iOS ou Windows) alterne os comandos das linhas 17 ↔ 18.

network_stats.db

- Banco de dados gerado a partir da execução local onde são armazenados os resultados do monitoramento.

## Autor

- André Ferreira
- E-mail: andre.luuiz.ferreira@gmail.com
