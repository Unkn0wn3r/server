import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hauptkanal_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hauptkanal_server_socket.bind((socket.gethostname(), 1234))#haupt port
hauptkanal_server_socket.listen(100)

server_socket.bind(('192.168.1.127', 1944))#1
server_socket.bind(('192.168.1.127', 1674))#2
server_socket.bind(('192.168.1.127', 1932))#3
server_socket.bind(('192.168.1.127', 1987))#4
server_socket.bind(('192.168.1.127', 1154))#5
server_socket.bind(('192.168.1.127', 1285))#6
server_socket.bind(('192.168.1.127', 1239))#7
server_socket.bind(('192.168.1.127', 9392))#8
server_socket.bind(('192.168.1.127', 1323))#9
server_socket.bind(('192.168.1.127', 7777))#10

server_socket.listen(10)

while True:
  (client_socket, addr) = server_socket.accept()
  hauptkanal_server_socket.send(client_socket.recv(1024))
