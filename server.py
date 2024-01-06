import socket

ip = "127.0.0.1"
port = 7777

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((ip, port))
server.listen(5)

print("[*] Ожидание подключения...")

client, address = server.accept()
print('Подключение по адресу: ', address)
# data = client.recv(1024).decode('utf-8') # получение данных от клиента в байтовом формате и их декод в utf-8
#
# print(data)

while True:
    com = input(str('#>' ))

    if com == 'exit':
        client.send(com.encode())
        break







