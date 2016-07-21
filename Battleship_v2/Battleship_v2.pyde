from random import *

listSize = 5
ships = 2
boardWidth = 500
boardHeight = 500
turnLimit = 10

board = [] #Stores Hits,  Misses, and empties
turns = 0 #sets the turn limit

for i in range(listSize):
    board.append(["0"] * listSize)

for m in range(ships):    
    board[randint(0, len(board) - 1)][randint(0, len(board[0]) - 1)] = "S" #Randomly places ship

def keyPressed():
    print("Set your difficulty: 1 = Easy, 2 = Medium, 3 = Hard")
    
    if key == "1":
        listSize = 3
        ships = 1
        boardWidth = 300
        boardHeight = 300
        turnLimit = 4
    if key == "2":
        listSize = 5
        ships = 2
        boardWidth = 500
        boardHeight = 500
        turnLimit = 10
    if key == "3":
        listSize = 10
        ships = 31  
        boardWidth = 1000
        boardHeight = 1000
        turnLimit = 20    

def setup():
    size(boardWidth, boardHeight)

# Initializes the Board and changes it based in hits, misses, and winning    
def initial_board():
    x = 0
    for j in range(listSize):
        y = 0
        for k in range(listSize):
            if board[j][k] == "0" or board[j][k] == "S":
                fill(0, 0, 255)
                rect(x, y, 100, 100)
            elif board[j][k] == "X":
                fill(255, 0, 0)
                ellipse(x + 50, y + 50, 100, 100)
            elif board[j][k] == "Z":
                    fill(255, 255, 255)
                    rect(x + 100/3, y, 33.33, 100)
            y = y + 100
        x = x + 100
          
def mousePressed():
    xM = mouseX
    yM = mouseY
    global turns
    
    if board[int(xM / 100)][int(yM / 100)] == "0":
        board[int(xM / 100)][int(yM / 100)] = "X"
        turns = turns + 1
        print("Miss!")
        
    elif board[int(xM / 100)][int(yM / 100)] == "X":
        print("Already Targeted")
        
    elif board[int(xM / 100)][int(yM / 100)] == "S":
        board[int(xM / 100)][int(yM / 100)] = "Z"
        turns = "stop"
        print("Hit!")    

def draw():
    if turns < turnLimit:
        initial_board()
    
    elif turns == "stop":
        background(255, 255, 255)
        #textSize(50)
        text("You Win!", 150, 250)
            
    else:
        background(255, 255, 255)
        fill(255, 0, 0)
        textSize(50)
        text("Gameover!", 150, 250)