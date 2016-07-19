from random import *

score = 0
x = 200
y = 200
Gameover = False
xChange = randrange(-2, 3)
print("asdf")

if xChange == 0:
    yChange = randrange(-2, 3)
    while yChange == 0:
        yChange = randrange(-2, 3)

elif xChange == -2 or xChange == 2:
    yChange = randrange(-2, 3)
    while yChange == -2 or yChange == 2:
        yChange = randrange(-2, 3)
        
else:
    yChange = randrange(-2, 3)        

def setup():
    size(400, 400)
    background(255, 255, 255)
    
def draw():
    
    xM = mouseX
    global score
    global x
    global y
    global Gameover
    global xChange
    global yChange
    
    background(255, 255, 255) 
    fill(0, 0, 255)
    ellipse(x, y, 50, 50)
    rect(xM, 350, 100, 20)
    text(str(score), 20, 20, 20)
    
    if Gameover == False:
        x = x + xChange
        y = y + yChange
        
        if x <= 25:
            xChange = randrange (1, 3)
            if xChange == 2:
                if yChange < 0:
                    yChange = -1
                elif yChange > 0:
                    yChange = 1
                elif yChange == 0:
                    while yChange == 0:
                        yChange = randrange(-1, 2)
            else:                
                if yChange < 0:
                    yChange = randrange(-2, 0)
                elif yChange > 0:
                    yChange = randrange(1, 3)
                elif yChange == 0:
                    while yChange == 0:
                        yChange = randrange(-2, 3)
                
        if x >= 375:
            xChange = randrange(-2, 0)
            if xChange == -2:
                if yChange < 0:
                    yChange = -1
                elif yChange > 0:
                    yChange = 1
                elif yChange == 0:
                    while yChange == 0:
                        yChange = randrange(-1, 2)
            else:                
                if yChange < 0:
                    yChange = randrange(-2, 0)
                elif yChange > 0:
                    yChange = randrange(1, 3)
                elif yChange == 0:
                    while yChange == 0:
                        yChange = randrange(-2, 3)
                
        if y <= 25:
            yChange = randrange(1, 3)
            if yChange == 2:
                if xChange < 0:
                    xChange = randrange(-1, 1)
                elif xChange > 0:
                    xChange = randrange(0, 2)
                elif xChange == 0:
                    while xChange == 0:
                        xChange = randrange(-1, 2)
            else:                
                if xChange < 0:
                    xChange = randrange(-2, 1)
                elif xChange > 0:
                    xChange = randrange(0, 3)
                elif xChange == 0:
                    while xChange == 0:
                        xChange = randrange(-2, 3)
        
        if x <= mouseX + 100 and x >= mouseX:   
            if y >= 325:
                yChange = randrange(-2, 0)
                if yChange == -2:
                    if xChange < 0:
                        xChange = randrange(-1, 1)
                    elif xChange > 0:
                        xChange = randrange(0, 2)
                    elif xChange == 0:
                        while xChange == 0:
                            xChange = randrange(-1, 2)
                else:                
                    if xChange < 0:
                        xChange = randrange(-2, 1)
                    elif xChange > 0:
                        xChange = randrange(0, 3)
                    elif xChange == 0:
                        while xChange == 0:
                            xChange = randrange(-2, 3)
                score = score + 1           
        if y >= 375:
            Gameover = True
            text("Gameover!",200,200,30)