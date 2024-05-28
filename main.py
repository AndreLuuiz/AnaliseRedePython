import os
import psutil
from db_connection import save_stats_to_db

def list_local_interfaces():
    interfaces = psutil.net_if_addrs()
    active_interfaces = []
    for interface, addrs in interfaces.items():
        stats = psutil.net_if_stats()[interface]
        if stats.isup:
            active_interfaces.append(interface)
    return active_interfaces

def execute_locally(interface):
    print(f"Executando captura de pacotes localmente na interface: {interface}...")
    print("Por favor,  caso utilize Linux ou iOS insira a senha de superusuário para continuar.")
    # os.system(f" sudo python capture_packets.py {interface}") # Para executar em Linux/iOS utilize este comando
    os.system(f"python capture_packets.py {interface}")  # Para executar em Windows utilize este comando
    print(f"\nPacotes disponíveis após captura:\n")
    os.system("python analyze_traffic.py")

def execute_with_docker(interface="eth0"):
    print(f"Construindo e executando o container Docker na interface {interface}...")
    os.system("docker build -t traffic-analyzer .")
    os.system(f"docker run --net=host --privileged -e INTERFACE={interface} traffic-analyzer")

def main():
    print("Escolha o modo de execução da aplicação:")
    print("1. Executar localmente")
    print("2. Executar com Docker")

    choice = input("Digite 1 ou 2: ")

    if choice == '1':
        interfaces = list_local_interfaces()
        if interfaces:
            print("Interfaces de rede ativas disponíveis:")
            for idx, iface in enumerate(interfaces):
                print(f"{idx + 1}. {iface}")

            iface_choice = input("Escolha uma interface de rede pelo número: ")
            try:
                iface_choice = int(iface_choice) - 1
                interface = interfaces[iface_choice]
            except (ValueError, IndexError):
                print(f"\nEscolha inválida. A interface {iface_choice + 1} não existe.\n")
                raise SystemExit

            execute_locally(interface)
            save_stats_to_db('captured_packets.json', 'network_stats.db')
            os.remove('captured_packets.json')
        else:
            print("\nNenhuma interface de rede ativa disponível encontrada.\n")
    elif choice == '2':
        execute_with_docker()
    else:
        print("\nOpção inválida. Por favor, escolha 1 ou 2.\n")

if __name__ == "__main__":
    main()