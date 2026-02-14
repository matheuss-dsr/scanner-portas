import socket
import sys
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

def scan_port(ip, port, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        return port, result == 0
    except:
        return port, False

def main():
    parser = argparse.ArgumentParser(description="Scanner de portas TCP simples")
    parser.add_argument("target", help="IP ou domínio para escanear")
    parser.add_argument("-p", "--ports", default="1-1024",
                        help="Portas a escanear (ex: 80,443 ou 1-1000)")
    parser.add_argument("-t", "--threads", type=int, default=100,
                        help="Quantidade de threads (padrão: 100)")
    
    args = parser.parse_args()
    
    print(f"[*] Iniciando scan em {args.target} às {datetime.now()}")
    
    # Tratamento das portas
    ports = []
    if '-' in args.ports:
        start, end = map(int, args.ports.split('-'))
        ports = range(start, end + 1)
    else:
        ports = [int(p) for p in args.ports.split(',')]
    
    open_ports = []
    
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        results = executor.map(lambda p: scan_port(args.target, p), ports)
        
        for port, is_open in results:
            if is_open:
                print(f"[+] Porta {port} está ABERTA")
                open_ports.append(port)
                print(f"[-] Porta {port} fechada")
    
    if open_ports:
        print(f"\nPortas abertas encontradas: {open_ports}")
    else:
        print("\nNenhuma porta aberta encontrada.")

if __name__ == "__main__":
    main()