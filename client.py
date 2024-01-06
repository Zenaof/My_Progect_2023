import socket

ip = "127.0.0.1"
port = 7777

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((ip, port))
print('Conected...')

while True:
    com = server.recv(1024).decode()

    if com == 'exit':
        break






