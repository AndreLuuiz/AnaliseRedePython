from collections import Counter
import json
import os

# Carregar pacotes capturados
if os.path.exists('captured_packets.json'):
    with open('captured_packets.json', 'r') as f:
        captured_packets = json.load(f)
else:
    print('Nenhum pacote encontrado!\n')
    exit()

# Número total de pacotes capturados
total_packets = len(captured_packets)

# Número de pacotes por protocolo
protocols = [pkt['proto'] for pkt in captured_packets]
protocol_count = Counter(protocols)

# Top 5 endereços IP de origem com mais tráfego
src_ips = [pkt['src_ip'] for pkt in captured_packets]
top_src_ips = Counter(src_ips).most_common(5)

# Top 5 endereços IP de destino com mais tráfego
dst_ips = [pkt['dst_ip'] for pkt in captured_packets]
top_dst_ips = Counter(dst_ips).most_common(5)

# Formatação da saída
print("Estatísticas:")
print(f"Total de Pacotes Capturados: {total_packets}\n")

print("Pacotes por Protocolo:")
for proto, count in protocol_count.items():
    print(f"Protocolo Nº {proto}: {count} packets")

print("\nTop 5 IP's de Origem:")
for ip, count in top_src_ips:
    print(f"{ip}: {count} packets")

print("\nTop 5 IP's de Destino:")
for ip, count in top_dst_ips:
    print(f"{ip}: {count} packets")

print("\n----------")
print("\nPacotes Armazenados no Banco de Dados:")
for packet in captured_packets:
    print(f"IP Origem: {packet['src_ip']}, IP Destino: {packet['dst_ip']}, Protocolo: {packet['proto']}, Tamanho: {packet['size']}")


