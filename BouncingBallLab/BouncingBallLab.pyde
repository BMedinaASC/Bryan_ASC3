from random import *

x = 200
y = 200
xChange = randrange(-2, 3)

if xChange == 0:
    yChange = randrange(-2, 3)
    while yChange == 0:
        yChange = randrange(-2, 3)

elif xChange == -2 or xChange == 2:
    yChange = randrange(-2, 3)
    while yChange == -2 or xChange == 2:
        yChange = randrange(-2, 3)
        
else:
    yChange = randrange(-2, 3)        

def setup():
    size(400, 400)
    background(255, 255, 255)
    
def draw():
    global x
    global y
    global xChange
    global yChange
    
    background(255, 255, 255) 
    fill(255, 0, 0)
    ellipse(x, y, 50, 50)
    x = x + xChange
    y = y + yChange
    
    if x <= 25:
        xChange = randrange (1, 3)
        if xChange == 2:
            if yChange < 0:
                yChange = randrange(-1, 1)
            elif yChange > 0:
                yChange = randrange(0, 2)
            elif yChange == 0:
                while yChange == 0:
                    yChange = randrange(-1, 2)
        else:                
            if yChange < 0:
                yChange = randrange(-2, 1)
            elif yChange > 0:
                yChange = randrange(0, 3)
            elif yChange == 0:
                while yChange == 0:
                    yChange = randrange(-2, 3)
            
    if x >= 375:
        xChange = randrange(-2, 0)
        if xChange == -2:
            if yChange < 0:
                yChange = randrange(-1, 1)
            elif yChange > 0:
                yChange = randrange(0, 2)
            elif yChange == 0:
                while yChange == 0:
                    yChange = randrange(-1, 2)
        else:                
            if yChange < 0:
                yChange = randrange(-2, 1)
            elif yChange > 0:
                yChange = randrange(0, 3)
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
            
    if y >= 375:
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
    
     