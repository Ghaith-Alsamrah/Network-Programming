import socket

sockS = socket.socket(family=socket.AF_INET, type= socket.SOCK_STREAM)
sockS.bind(('127.0.0.1', 60003))
sockS.listen(1)


while True:
    print('\nlistening...\n')
    (sockC, addr) = sockS.accept()
    print('Connection from {}'.format(addr))
    while True:
        data = sockC.recv(1024)
        if not data:
            break
        print('Received:',data.decode('ascii'))
        answer = 'Thanks for the data!'
        sockC.sendall(bytearray(answer, 'ascii'))
        print ('answered:', answer)
    sockC.close()
    print('client {} disconnected'.format(addr))