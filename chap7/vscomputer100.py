import random as R
turn = 0              #human 0, computer 1
board = []
boardcal = [0,0,0,0,0,0,0,0,0]      # O == 1 , X == 5
bingo = 0
draw = 0
computer = 0
row = [0,0,0]
col = [0,0,0]
x = [0,0,0]
humanwin = 0
computerwin = 0
drawdraw = 0
count = 0
def display_instruct() :
    print("welcome to the greatest intellectual challenge of all time : Tic-Tac-Toe.")
    print("This will be a showdown between your human brain and my silicon processor.\n\n")
    print("You will make your move know be entering a number, 0 - 8. The number")
    print("will correspond to the board position as illustrated:")
    print("\n           0 | 1 | 2")
    print("           ----------")
    print("           3 | 4 | 5")
    print("           ----------")
    print("           7 | 8 | 9")
    print("Prepare yourself, human.  The ultimate battle is about to begin.")

def pieces() :
    f = input("Do you require the first move? (y/n):")
    if f == "y" :
        return 0
    else :
        return 2

def new_board():
    board.clear()
    for i in range(9):
        board.append(" ")

def display_board() :
    print("          ",board[0],"|",board[1],"|",board[2])
    print("          -----------")
    print("          ",board[3],"|",board[4],"|",board[5])
    print("          -----------")
    print("          ",board[6],"|",board[7],"|",board[8])

def winner(bingo) :              #미완성
    row[0] = boardcal[0] + boardcal[1] + boardcal[2]
    row[1] = boardcal[3] + boardcal[4] + boardcal[5]
    row[2] = boardcal[6] + boardcal[7] + boardcal[8]

    col[0] = boardcal[0] + boardcal[3] + boardcal[6]
    col[1] = boardcal[1] + boardcal[4] + boardcal[7]
    col[2] = boardcal[2] + boardcal[5] + boardcal[8]

    x[0] = boardcal[0] + boardcal[4] + boardcal[8]
    x[1] = boardcal[2] + boardcal[4] + boardcal[6]
    x[2] = 0

    for i in range(3) :
        if row[i] == 3 or col[i] == 3 or x[i] == 3:
            return 1
        if row[i] == 15 or col[i] == 15 or x[i] == 15:
            return 2

def colbingo(num) :
    for i in range(3) :
        if col[i] == num :
            for j in range(3) :
                if boardcal[i+(j*3)] == 0:
                    computer = i+(j*3)
                    return computer
def rowbingo(num) :
    for i in range(3) :
        if row[i] == num :
                for j in range(3) :
                    if boardcal[(i*3)+j] == 0:
                        computer = (i*3)+j
                        return computer

def algorism(computer) :
    num = 0
    if boardcal[4] == 0 :
        return 4
    else :
        computer = R.randint(0,8)
        for i in range(3) :                 #Priority
            if col[i] == 10 :
                computer = colbingo(10)
                num = 10
                break
            elif row[i] == 10 :
                computer = rowbingo(10)
                num = 10
                break
            else :
                continue
        for i in range(3) :
            if col[i] == 2 and num == 0:
                computer = colbingo(2)
                num = 2
                break
            elif row[i] == 2 and num == 0:
                computer = rowbingo(2)
                num = 2
                break
            else :
                continue
        for i in range(3) :
            if col[i] == 5 and num == 0 :
                computer = colbingo(5)
                break
            elif row[i] == 5 and num == 0 :
                computer = rowbingo(5)
                break
            else :
                continue
    return computer
        


#실행
while count < 100 :
    new_board()
    turn = R.randint(0,2)
    while 1 :
        if turn == 0 :
            number = R.randint(0,8)
            board[number] = "o"
            boardcal[number] = 1
            draw += 1
            turn = 1
        else :
            computer = algorism(computer)
            while 1 :
                if board[computer] == "o" or board[computer] == "x" :
                    computer = algorism(computer)
                else :
                    board[computer] = "x"
                    boardcal[computer] = 5
                    draw += 1
                    turn = 0
                    break

        bingo = winner(bingo)

        if bingo == 1 :
            humanwin += 1
            break
        elif bingo == 2:
            computerwin += 1
            break
        elif draw == 9 :
            drawdraw += 1
            break
        else :
            continue
    count += 1
print("human =",humanwin,"computer =",computerwin,"draw =",drawdraw)