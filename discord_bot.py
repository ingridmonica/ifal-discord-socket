import discord
import socket
import argparse
import aiohttp

# Configurar argumentos da linha de comando
parser = argparse.ArgumentParser(description='Bot do Discord')
parser.add_argument('--host', default='127.0.0.1', help='Endereço do servidor socket')
parser.add_argument('--port', type=int, default=10000, help='Porta do servidor socket')
args = parser.parse_args()

HOST = args.host  # Endereço do servidor socket
PORT = args.port  # Porta do servidor socket    

# Token do bot do Discord
TOKEN = 'seu_token_bot'

intents = discord.Intents.default()
intents.message_content = True  # Habilita a leitura do conteúdo das mensagens

# Cria um cliente do Discord
client = discord.Client(intents=intents)

# Função para buscar citação aleatória da API dummyJSON
async def fetch_random_quote():
    # URL do endpoint da API que fornece uma citação aleatória
    url = 'https://dummyjson.com/quotes/random'
    
    # Cria uma sessão HTTP assíncrona
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                # Converte a resposta JSON em um dicionário Python
                data = await response.json()
                # Retorna a citação obtida
                return data['quote']
            else:
                # Retorna uma mensagem de erro se a citação não puder ser obtida
                return "Não foi possível obter uma citação no momento."

# Enviar mensagem para um canal do Discord
async def enviar_para_discord(message, content):
    if message.guild:
        await message.channel.send(content)
    else:
        print("Mensagem recebida fora de um canal de servidor.")

# Enviar mensagem para o servidor socket
async def enviar_para_socket(message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))  # Conecta ao servidor socket
            client_socket.sendall(message.content.encode())  # Envia mensagem
            resposta = client_socket.recv(1024)  # Recebe resposta
            await enviar_para_discord(message, resposta.decode())  # Envia resposta ao Discord
    except Exception as e:
        print(f"Erro ao enviar mensagem para o socket: {e}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Ignora mensagens do próprio bot

    if message.content.lower() == 'hello':
        await message.channel.send(f'Hello, {message.author.name}!') # Envia mensagem 'Hello <nome-usr>'

    if message.content.lower().startswith('ping'):
        await enviar_para_socket(message)  # Envia mensagem 'ping' ao servidor socket
    elif message.content.lower() in ['pedra', 'papel', 'tesoura']:
        await enviar_para_socket(message)  # Envia comando de 'pedra', 'papel' ou 'tesoura' ao servidor socket
    elif message.content.lower() == '!quote':
        quote = await fetch_random_quote()
        await message.channel.send(quote)
    
client.run(TOKEN)   