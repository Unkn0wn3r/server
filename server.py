import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hauptkanal_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hauptkanal_server_socket.bind((socket.gethostname(), 1234))#haupt port
hauptkanal_server_socket.listen(100)

server_socket.bind((socket.gethostname(), 1944))#1
server_socket.bind((socket.gethostname(), 1674))#2
server_socket.bind((socket.gethostname(), 1932))#3
server_socket.bind((socket.gethostname(), 1987))#4
server_socket.bind((socket.gethostname(), 1154))#5
server_socket.bind((socket.gethostname(), 1285))#6
server_socket.bind((socket.gethostname(), 1239))#7
server_socket.bind((socket.gethostname(), 9392))#8
server_socket.bind((socket.gethostname(), 1323))#9
server_socket.bind((socket.gethostname(), 7777))#10

server_socket.listen(10)

while True:
  (client_socket, addr) = server_socket.accept()
  hauptkanal_server_socket.send(client_socket.recv(1024))
