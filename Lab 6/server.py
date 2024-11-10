import socket

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sock.bind (('127.0.0.1', 60004))
sock.listen(1)

while True: 
    print ('\n Listening.... \n')

    (sockC,addr) = sock.accept()
    
    message = sockC.recv(1024)
    
    message = message.decode('ascii')
    print (message)
    sockC.sendall(bytearray("HTTP/1.1 200 ok \n", "ASCII "))
    sockC.sendall(bytearray("\n", "ASCII"))
    sockC.sendall(bytearray(f"""<html>\n <body>
                            <h1> Your browser send the following message </h1> 
                             <pre>{message} </pre> 
                             </body> </html>"""
                            
                            
                            
                            
                            , "ASCII"))
    continue

