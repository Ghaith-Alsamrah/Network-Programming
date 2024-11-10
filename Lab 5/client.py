import socket

sock = socket.socket(family=socket.AF_INET, type = socket.SOCK_STREAM)
sock.connect (('127.0.0.1', 60003))

message = input ('Type your message')
sock.sendall(bytearray(message, 'ascii'))
print ('sent:', message)

data = sock.recv(1024)
print('recieved:', data.decode ('ascii'))

sock.close