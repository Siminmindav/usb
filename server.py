import socket
import threading

# Server setup
HOST = "secretz"  # Localhost
PORT = 0     # Port for communication

server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

# Broadcast message to all clients
def broadcast(message, _client=None):
    for client in clients:
        if client != _client:  # don't send back to sender
            client.send(message)

# Handle messages from clients
def handle(client):
    while True:
        try:
            message = client.recv(1234)
            broadcast(message, client)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast(f"{nickname} left the chat!".encode("utf-8"))
            break

# Accept new clients
def receive():
    print("Server is running and listening...")
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("NICK".encode("utf-8"))
        nickname = client.recv(1024).decode("utf-8")
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode("utf-8"))
        client.send("Connected to the server!".encode("utf-8"))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
