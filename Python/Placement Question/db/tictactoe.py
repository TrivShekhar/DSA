class player():
    symbol=""
    moves=[]
    win=False
game=[["","",""] for i in range(3)]
p1 = player()
p1.symbol="X"
p2 = player()
p2.symbol="Y"
entries=0
def checkwin(player,row,col):
    i=0
    while(i<3):
        if(game[row][i]!=player.symbol):
            break
        i+=1
    if(i==3):
        return True
    i=0
    while(i<3):
        if(game[i][col]!=player.symbol):
            break
        i+=1
    if(i==3):
        return True
    if(row+col==2):
        roww=0
        coll=2
        while(coll>=0 and roww<=2):
            if(game[roww][coll]!=player.symbol):
                break
            roww+=1
            coll-=1
        if(roww==3):
            return True
    if(row==col):
        roww=0
        coll=0
        while(row < 3 and col <3):
            if(game[row][col]!=player.symbol):
                break
        if(row==3):
            return True


def checkvalidity(row,col):
    if(game[row][col]!=""):
        print("The feild is already filled retry")
        return False
    elif(row>=3 or col>=3 or row<0 or col<0):
        print("Wrong Entry")
        return False
    else: 
        return True
def printGame(game):
    for i in game:
        print(i)
    
while(True):
    if(input("Enter q if wanting to quit")=="q"):
        break
    printGame(game)
    print("Player 1's turn")
    while(True):
        row,col = map(int,input("Enter Row and column").split())
        if(checkvalidity(row,col)):
            p1.moves.append((row,col))
            game[row][col]=p1.symbol
            break
        else:
            continue
    
    printGame(game)    
    entries+=1
    if(entries>=5):
        if(checkwin(p1,row,col)):
            print("Player 1 Wins")
            break
        if(entries==9):
            print("Tie")
            break
    print("Player 2's turn")
    while(True):
        row,col = map(int,input("Enter Row and column").split())
        if(checkvalidity(row,col)):
            p2.moves.append((row,col))
            game[row][col]=p2.symbol
            break
        else:
            continue
    printGame(game)
    entries+=1
    if(entries>=5 and checkwin(p2,row,col)):
        print("Player 2 Wins")
        break

    

    
    
        

