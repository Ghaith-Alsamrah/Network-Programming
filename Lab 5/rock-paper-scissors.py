import socket 

def checkIfWinner (moveA, moveB):
    if(moveA == moveB) :
        return 'Draw'
    if (moveA == 'R' and moveB == 'S') or \
       (moveA == 'S' and moveB == 'P') or \
       (moveA == 'P' and moveB == 'R'):
        return 'A'
    else: 
        return 'B'




sock = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
score = 0 
gameStillOn = True
theirScore = 0
choice = input('Do you want to be the Server ("S") or the Client ("C") \n')


def printResult(result):
    global score
    global theirScore 
    if (result == 'A'):
         
        score += 1
        return ('You win, the score is ({},{})'.format(score,theirScore))
    elif (result == 'B'):
        
        theirScore +=1 
        return ('They win, the score is ({},{})'.format(score,theirScore))
    else:
        return ("It's a draw, the score is ({},{})".format(score,theirScore))


def checkIfMoveValid(move): 
    if (move not in ('R','P','S')):
        return False
if (choice == 'S'):
    sock.bind(('127.0.0.1', 60003))
    sock.listen(1)
    print ('Waiting for the other player')
    (sockC, adrr) = sock.accept()
    print ('Player 2 has connected')
    while gameStillOn:  
        move = input('Make a move \n')
        checkIfMoveValid(move)
        sockC.sendall(bytearray(move,'ascii'))
        data = sockC.recv(1024) 
        if not data: 
            break
        theirMove = data.decode('ascii')
        print(theirMove)
        result = checkIfWinner(move,theirMove)
        theirResult = checkIfWinner(theirMove,move)
        
        if(result):
            resultMessage = printResult(result)
            sockC.sendall(bytearray(theirResult,'ascii'))
            print(resultMessage)
            continuePlaying = input('Do you still wanna play')
            if (continuePlaying == 'Y'):
                sockC.sendall(bytearray('Do you still wanna play?', 'ascii'))
                stillWannapPlay = sockC.recv(1028)
                if (stillWannapPlay.decode('ascii')=='N'):
                    gameStillOn = False
                    break
                continue
            elif(continuePlaying == 'N'):
                sockC.sendall(bytearray(str(gameStillOn), 'ascii'))
                break
        





elif (choice == 'C'):
    ipAdress = input("What's the IP adress?")
    ipAdress = str (ipAdress)
    sock.connect((ipAdress, 60003))
    print ('Player 2 has connected')
    while gameStillOn: 
        data = sock.recv(1024) 
        print('player one made a move')
        print(data.decode('ascii'))
        if not data: 
            break
        else:
            move = input('Make a move \n')
            while move not in ('R', 'P', 'S'): 
                move = input ('Please play a valid move')
            sock.sendall(bytearray(move,'ascii'))
            result = sock.recv(1024)
            print (printResult(result.decode('ascii')))
            continuePlayingC = sock.recv(1024)
            continuePlayingC = continuePlayingC.decode('ascii')
            print (continuePlayingC)
            continuePlayingC = input ('')
            sock.sendall(bytearray(continuePlayingC,'ascii'))
            if (continuePlayingC == 'Y'):
                continue
            elif (continuePlayingC == 'N'): 
                gameStillOn = False 





