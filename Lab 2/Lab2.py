from posixpath import split


file = open ('score2.txt', 'r') 

players = []


for line in file: 
    currentRow = line.split() 
    currentRow[-1] = int (currentRow[-1])
    if not players: 
        players.append(currentRow)

    else: 
        for i in players: 
            if i[2:-1] == currentRow[2:-1]:
                i[-1] += currentRow[-1]
                break
        else: 
            players.append(currentRow)

winner = players[0]
for player in players: 
    for i in players: 
        if winner[-1] < i[-1]: 
            winner = i
print (winner[2:])


######              The winner is Maria Johansson with 37 points            ###### 

