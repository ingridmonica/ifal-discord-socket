# ifal-discord-socket
 Discord Bot with socket server

# Configuração do Bot do Discord

Este repositório contém um bot do Discord que utiliza Python e possui comunicação via servidor socket. Siga as instruções abaixo para configurar o ambiente e executar o bot.

## Criar Bot 
1. Acessar o Portal do Desenvolvedor do Discord e (se não possuir um bot) você deve criar um aplicativo e configurar um bot conforme o desafio.

## Configuração do Ambiente

1. **Virtual Environment**: Crie um ambiente virtual Python para isolar as dependências do projeto. Execute o seguinte comando no terminal:

    ```bash
    python -m venv venv
    ```

2. **Ativação do Ambiente Virtual**: Ative o ambiente virtual. No Windows, use:

    ```bash
    venv\Scripts\activate
    ```

    No macOS/Linux, use:

    ```bash
    source venv/bin/activate
    ```

3. **Instalação de Dependências**: Instale as dependências do projeto usando o arquivo `requirements.txt`. Execute:

    ```bash
    pip install -r requirements.txt
    ```

## Configuração do Bot do Discord

1. **Preenchimento da Chave do Bot**: No arquivo `discord_bot.py`, insira a chave do seu bot do Discord na variável `TOKEN`. Certifique-se de que o seu bot tenha imissões adequadas.

2. **Execução do Servidor Socket**: Antes de executar o bot, é necessário executar o arquivo `socket_server.py` para iniciar o servidor de socket. Execute:

    ```bash
    python socket_server.py
    ```

3. **Execução do Bot**: Agora, execute o arquivo `discord_bot.py` para iniciar o bot do Discord:

    ```bash
    python discord_bot.py
    ```

Se tudo estiver configurado corretamente, seu bot do Discord deve estar online e pronto para uso!

## Funcionalidades
- Responder ao comando ping com pong.
- Jogar o jogo &quot;Pedra, Papel, Tesoura&quot; com os usuários, determinando o vencedor baseado na escolha do usuário e do servidor.
- Enviar e receber mensagens entre o bot e o servidor socket, processando as respostas adequadamente.
- Responder ao comando !quote com uma citação aleatória que foi acessada por uma API externa Dummyjson.
- Responder a saudação “Hello” com Hello e o nome do usuário que iniciou a comunicação.

## Membros da Equipe

- Ingrid Mônica da Silva Bezerra
- Jardel Cleyson da Silva
- Karla Cristina de Sousa Araújo
- Marcus Vinicius Gomes Pestana
