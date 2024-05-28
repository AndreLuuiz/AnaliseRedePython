import sys
import psutil
from scapy.all import sniff, IP
import json

# Mapeamento de números de protocolo para seus nomes
protocol_mapping = {
    1: '1 - ICMP',
    2: '2 - IGMP',
    6: '6 - TCP',
    17: '17 - UDP',
    # Adicione outros protocolos conforme necessário
}

# Função de callback para processar cada pacote capturado
def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        size = len(packet)
        protocol = protocol_mapping.get(proto, str(proto))

        # Armazenar informações do pacote em um dicionário
        packet_info = {
            'src_ip': src_ip,
            'dst_ip': dst_ip,
            'proto': protocol,
            'size': size
        }

        captured_packets.append(packet_info)

# Lista para armazenar os pacotes capturados
captured_packets = []

# Verificar a interface de rede
def check_interface(interface):
    if interface not in psutil.net_if_addrs():
        raise ValueError(f"\nA interface de rede escolhida '{interface}' não possui pacotes!")

# Interface de rede a ser monitorada
if len(sys.argv) < 2:
    print("Uso: python capture_packets.py <interface>")
    sys.exit(1)

network_interface = sys.argv[1]

# Verificar se a interface existe
try:
    check_interface(network_interface)
except ValueError as e:
    print(e)
    sys.exit(1)

# Iniciando a captura de pacotes
print(f"\nCapturando pacotes na interface: {network_interface}...")
# Capturar os 100 primeiros pacotes
sniff(iface=network_interface, prn=packet_callback, count=100)
print("Captura finalizada!")

# Salvando pacotes capturados em um arquivo para análise posterior
with open('captured_packets.json', 'w') as f:
    json.dump(captured_packets, f)

print("\nPacotes capturados salvos em 'captured_packets.json'.")