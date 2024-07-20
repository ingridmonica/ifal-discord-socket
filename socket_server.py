import socket
import argparse
import random

# Configurar argumentos da linha de comando
parser = argparse.ArgumentParser(description='Servidor de Socket')
parser.add_argument('--host', default='127.0.0.1', help='Endereço do servidor')
parser.add_argument('--port', type=int, default=10000, help='Porta do servidor')
args = parser.parse_args()

HOST = args.host  # Endereço do servidor
PORT = args.port  # Porta do servidor

# Função para jogar Pedra, Papel, Tesoura
def jogar_pedra_papel_tesoura(escolha_usuario):
    escolhas = ['pedra', 'papel', 'tesoura']
    escolha_servidor = random.choice(escolhas)
    if escolha_usuario == escolha_servidor:
        return f'Bot: {escolha_servidor} \nResultado: Empate! Ambos escolheram {escolha_usuario}.'
    elif (escolha_usuario == 'pedra' and escolha_servidor == 'tesoura') or \
         (escolha_usuario == 'papel' and escolha_servidor == 'pedra') or \
         (escolha_usuario == 'tesoura' and escolha_servidor == 'papel'):
        return f'Bot: {escolha_servidor} \nResultado: Você ganhou! {escolha_usuario} vence {escolha_servidor}.'
    else:
        return f'Bot: {escolha_servidor} \nResultado: Você perdeu! {escolha_servidor} vence {escolha_usuario}.'
    
    
# Cria um socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))  # Liga o socket ao endereço e porta especificados
    server_socket.listen()  # Ouve por conexões recebidas

    print(f'Servidor socket escutando em {HOST}:{PORT}')

    while True:
        client_socket, addr = server_socket.accept()  # Aceita conexões entrantes
        with client_socket:
            print(f'Conexão recebida de {addr}')
            data = client_socket.recv(1024)  # Recebe dados do cliente

            # Processa a mensagem recebida
            try:
                message = data.decode().strip().lower()
                if message == "ping":
                    client_socket.sendall(b'pong')  # Envia resposta ao cliente
                elif message in ['pedra', 'papel', 'tesoura']:
                    resultado = jogar_pedra_papel_tesoura(message)
                    client_socket.sendall(resultado.encode())  # Envia resultado ao cliente
                else:
                    client_socket.sendall(b'Comando invalido')
            except UnicodeDecodeError:
                print("Erro ao decodificar a mensagem.")