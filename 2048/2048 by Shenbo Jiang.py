# Made by Shenbo Jiang
#
# steps
# 1. set up the board using list in lists and create a temporary board
# 2. create functions that merge left right up and down
# 3. Setup the board at the start of the game with two random values
# 4. set up the rounds of the game where the user will have the option
#    to merge any direction and display the board
# 5. set up adding new values
# 6. set up functions to test if the game is still on

import random
import copy

boardSize = 4



board = []
for i in range(boardSize):
    row = []
    for j in range(boardSize):
        row.append(0)
    board.append(row)

def pickNewValue():
    if random.randint(1, 10) == 1:
        return 4
    else:
        return 2

numNeeded = 2
while numNeeded > 0:
    rowNum = random.randint(0, boardSize - 1)
    colNum = random.randint(0, boardSize - 1)

    if board[rowNum][colNum] == 0:
        board[rowNum][colNum] = pickNewValue()
        numNeeded -= 1





def mergeOneRowL(row):
    for j in range(boardSize - 1):
        for i in range(boardSize - 1, 0, -1):
            if row[i - 1] == 0:
                row[i - 1] = row[i]
                row[i] = 0

    for i in range(boardSize - 1):
        if row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0
    for i in range(boardSize - 1, 0, -1):
        if row[i - 1] == 0:
            row[i - 1] = row[i]
            row[i] = 0
    return row

def merge_left(currentBoard):
    for i in range(boardSize):
        currentBoard[i] = mergeOneRowL(currentBoard[i])
    return currentBoard

def reverse(row):
    new = []
    for i in range(boardSize - 1, -1, -1):
        new.append(row[i])
    return new

def merge_right(currentBoard):
    for i in range(boardSize):
        currentBoard[i] = reverse(currentBoard[i])
        currentBoard[i] = mergeOneRowL(currentBoard[i])
        currentBoard[i] = reverse(currentBoard[i])
    return currentBoard


def transpose(currentBoard):
    for j in range(boardSize):
        for i in range(j, boardSize):
            if not i == j:
                temp = currentBoard[j][i]
                currentBoard[j][i] = currentBoard[i][j]
                currentBoard[i][j] = temp
    return currentBoard

def merge_up(currentBoard):
    currentBoard = transpose(currentBoard)
    currentBoard = merge_left(currentBoard)
    currentBoard = transpose(currentBoard)
    return currentBoard

def merge_down(currentBoard):
    currentBoard = transpose(currentBoard)
    currentBoard = merge_right(currentBoard)
    currentBoard = transpose(currentBoard)
    return currentBoard

def display():
    largest = board[0][0]
    for row in board:
        for element in row:
            if element > largest:
                largest = element

    numSpaces = len(str(largest))
    for row in board:
        currRow = "|"
        for element in row:
            if element == 0:
                currRow += numSpaces * " " + "|"
            else:
                currRow += " " * (numSpaces - len(str(element))) + str(element) + "|"
        print(currRow)
    print()

def gameWin():
    for row in board:
        if 2048 in row:
            return True
    return False

def gameLost():
    testBoard1 = copy.deepcopy(board)
    testBoard2 = copy.deepcopy(board)

    testBoard1 = merge_down(testBoard1)
    if testBoard1 == testBoard2:
        testBoard1 = merge_up(testBoard1)
        if testBoard1 == testBoard2:
            testBoard1 = merge_left(testBoard1)
            if testBoard1 == testBoard2:
                testBoard1 = merge_right(testBoard1)
                if testBoard1 == testBoard2:
                    return True
    return False


print("Welcome to 2048, 'w' is up, 'a' is left, 's' is down and 'd' is right. Start!!!")
display()

gameState = True



while gameState:
    currBoard = copy.deepcopy(board)
    validInput = True
    move = input("Which way do you want to move? ")
    move = move.upper()

    if move == "W":
        board = merge_up(board)
    elif move == "A":
        board = merge_left(board)
    elif move == "S":
        board = merge_down(board)
    elif move == "D":
        board = merge_right(board)
    else:
        validInput = False

    if currBoard == board:
        validInput = False
    
    if not validInput:
        print("Please input a valid move.")       
    else:
        if gameWin():
            print("You have WON!!!!")
            display()
        else:
            newnum = True
            while newnum == True:
                rowNum = random.randint(0, boardSize - 1)
                colNum = random.randint(0, boardSize - 1)

                if board[rowNum][colNum] == 0:
                    board[rowNum][colNum] = pickNewValue()
                    newnum = False
            display()
            if gameLost():
                print("Unfortunately you have ran out of possible moves, YOU LOST!!!")
                gameState = False