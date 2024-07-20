import socket
import json

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 10000))  # Liga o socket ao endereço e porta
    server_socket.listen(1)  # Ouve por conexões recebidas

    print("Server started, listening for connections...")

    while True:
        client_socket, address = server_socket.accept()  # Aceita conexões entrantes
        print(f"Connection from {address} established.")
        
        data = client_socket.recv(1024).decode()  # Recebe dados
        request = json.loads(data)  # Decodifica dados recebidos
        
        if request.get("command") == "ping":
            response = {"message": "Pong!"}
            client_socket.send(json.dumps(response).encode())  # Envia resposta

        client_socket.close()  # Fecha a conexão com o cliente

if __name__ == "__main__":
    main()
