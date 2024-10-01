import socket
import signal
import sys
from termcolor import colored

def def_handler(sig, frame):
    print(colored("\n\n Saliendo...\n", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def scan_port(ip, port):
    # Escanea un puerto específico en la dirección IP dada
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Timeout para la conexión
    result = sock.connect_ex((ip, port))

    if result == 0:

        print(colored(f"\n\n El puerto {port} está ABIERTO", "green"))

    sock.close()

if __name__ == "__main__":

    target_ip = input(colored("\nIntroduce la dirección IP a escanear: ", "blue")) # IP: 127.0.0.1
    start_port = int(input(colored("\nIntroduce el puerto inicial: ", "blue"))) # Puerto: 1
    end_port = int(input(colored("\nIntroduce el puerto final: ", "blue"))) # Puerto: 9999

    for port in range(start_port, end_port + 1):
        scan_port(target_ip, port)

