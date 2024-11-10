import socket
import select

port = 60003 
sockL = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
sockL.bind (("", port))
sockL.listen(1)

listOfSockets = [sockL]

print ("Listening on port {}".format(port))

while True:
    tup = select.select(listOfSockets, [], [])
    sock = tup[0][0]
    if sock == sockL: 
        (sockClient, addr) = sockL.accept()
        listOfSockets.append(sockClient)
        for s in listOfSockets:
            if s != sockL and s != sockClient:
                s.sendall(bytearray("{} has connetected".format(sockClient),'ascii'))
    else:
        data = sock.recv(1024)
        if not data:
            sock.close()
            listOfSockets.remove(sock)
            sockL.sendall(bytearray("{} has disconnected".format(sock), 'ascii'))
        else: 
            for s in listOfSockets:
                if s != sockL and s != sock:
                    s.sendall(data)

