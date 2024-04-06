print("WELCOME TO MY TIC-TAC-TOE GAME!!!")
print("COMPUTER SCIENCE INVESTIGATORY PROJECT BY AKSHIT RAJ GRADE XI F ROLL NO. 8 ")
board=[0,1,2,
       3,4,5,
       6,7,8,]
def printBoard(board):
    print(board[0],"|",board[1],"|",board[2])
    print("--|---|---")
    print(board[3],"|",board[4],"|",board[5])
    print("--|---|---")
    print(board[6],"|",board[7],"|",board[8])
printBoard(board)
p1='X'
p2='O'
def checkwinX():
    if board[0] == "X" and board[1] == "X" and board[2] == "X" or \
    board[3] == "X" and board[4] == "X" and board[5] == "X" or \
    board[6] == "X" and board[7] == "X" and board[8] == "X" or \
    board[0] == "X" and board[3] == "X" and board[6] == "X" or \
    board[1] == "X" and board[4] == "X" and board[7] == "X" or \
    board[4] == "X" and board[7] == "X" and board[8] == "X" or \
    board[0] == "X" and board[4] == "X" and board[8] == "X" or \
    board[2] == "X" and board[4] == "X" and board[6] == "X":

        
        print("Player 1 wins!")
        return True

    else:
        return False
def checkwinO():
    if board[0] == "O" and board[1] == "O" and board[2] == "O" or \
    board[3] == "O" and board[4] == "O" and board[5] == "O" or \
    board[6] == "O" and board[7] == "O" and board[8] == "O" or \
    board[0] == "O" and board[3] == "O" and board[6] == "O" or \
    board[1] == "O" and board[4] == "O" and board[7] == "O" or \
    board[4] == "O" and board[7] == "O" and board[8] == "O" or \
    board[0] == "O" and board[4] == "O" and board[8] == "O" or \
    board[2] == "O" and board[4] == "O" and board[6] == "O":

        
        print("Player 2 wins!")
        return True

    else:
        return False

def checkdraw():
    if board[0]== "X" and board[1]=="X" and board[4]== "X" and board[5]== "X" and board[6]== "X" or \
    board[1]== "X" and board[2]=="X" and board[3]== "X" and board[4]== "X" and board[8]== "X" or \
    board[2]== "X" and board[3]=="X" and board[4]== "X" and board[7]== "X" and board[8]== "X" or \
    board[0]== "X" and board[4]=="X" and board[5]== "X" and board[6]== "X" and board[7]== "X" or \
    board[1]== "X" and board[4]=="X" and board[5]== "X" and board[6]== "X" and board[8]== "X" or \
    board[1]== "X" and board[3]=="X" and board[4]== "X" and board[6]== "X" and board[8]== "X" or \
    board[0]== "X" and board[2]=="X" and board[3]== "X" and board[4]== "X" and board[7]== "X" or \
    board[0]== "X" and board[2]=="X" and board[4]== "X" and board[5]== "X" and board[7]== "X" or \
    board[0]== "X" and board[1]=="X" and board[5]== "X" and board[6]== "X" and board[7]== "X" or \
    board[1]== "X" and board[2]=="X" and board[5]== "X" and board[7]== "X" and board[8]== "X" or \
    board[1]== "X" and board[3]=="X" and board[5]== "X" and board[6]== "X" and board[8]== "X" or \
    board[0]== "X" and board[2]=="X" and board[3]== "X" and board[5]== "X" and board[7]== "X" or \
    board[0]== "X" and board[2]=="X" and board[3]== "X" and board[7]== "X" and board[8]== "X" or \
    board[0]== "X" and board[2]=="X" and board[5]== "X" and board[6]== "X" and board[7]== "X" or \
    board[1]== "X" and board[2]=="X" and board[3]== "X" and board[6]== "X" and board[8]== "X" or \
    board[0]== "X" and board[1]=="X" and board[5]== "X" and board[6]== "X" and board[8]== "X":
        print("It's a tie!")
        return True
    else:
        return False    
def play_again():
    print("Do you want to play again?")
    play_again = input()

    if play_again.upper() == 'Y':
        for p in board:
            board[p] = ' '
        return True
    else:
        print("Thanks for playing. See you next time!")
        return False
currentplayer=p1
winner=False
playing=True
count = 0
tie = False
p2playing=False
while playing:
    count+=1
    i1=int(input("Player 1, please input your block choice (0-8): "))
    if i1>=0 and i1<=8 and board[i1]==i1:
        board[i1]=currentplayer
        p2playing=True
    elif i1>=0 and i1<=8 and board[i1]!=i1:
        print("Oops! There is already a number on that spot!")
        continue
    elif i1<0 or i1>8:
        print("Invalid number. Enter valid response")
        continue
    printBoard(board)
    x=checkwinX()
    if checkwinX():
        x=True
        winner=True
        break
    if checkdraw():
        z=True
        tie=True
        break
    currentplayer=p2
    while p2playing:
        count+=1
        i2=int(input("Player 2, please input your block choice (0-8): "))
        if i2>=0 and i2<=8 and board[i2]==i2:
            board[i2]=currentplayer
            p2playing=False
        elif i2>=0 and i2<=8 and board[i2]!=i2:
            print("Oops! There is already a number on that spot!")
            continue
        else:
            print("Enter valid response")
            continue
        printBoard(board)
        y=checkwinO()
        currentplayer=p1
    if checkwinO():
        y=True
        winner=True
        break
    if checkdraw():
        z=True
        tie=True
        break

print("Thank You for playing my TIC TAC TOE game!")


    
    




    