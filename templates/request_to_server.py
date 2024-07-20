import socket
import json

# Endereço do servidor e porta
HOST = 'localhost'
PORT = 10000

data_to_send = {'command': 'ping'}  # Dados a serem enviados ao servidor

# Converter o JSON em bytes
json_data = json.dumps(data_to_send).encode()

# Cria um socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Conecta ao servidor
    s.sendall(json_data)  # Envia dados
    data = s.recv(1024)  # Recebe resposta

print('Recebido:', data.decode())  # Exibe resposta recebida
