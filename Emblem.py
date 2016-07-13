from Myro import *
init("sim")

s = 0.5

def square():
    i = 0
    while i < 4:
        forward(s, 10)
        turnBy(90)
        i = i + 1
        
def claw():
    forward(s, 3.9)
    turnBy(45)
    forward(s, 1)
    turnBy(45)
    forward(s, 1)
    turnBy(90)
    forward(s, 1)
    turnBy(60)
    forward(s, 1.1)
    turnBy(-45)
    forward(s, 3.3)

forward(s, 10)    
turnBy(90)
forward(s, 10)
turnBy(90)
penDown()            
square() 
forward(s, 5.5)
turnBy(90)
penUp()
forward(s, 5/3)

k = 0
while k < 3:
    penDown()
    turnBy(-45)
    claw()
    turnBy(-60)
    penUp()
    forward(s, 5/3)
    turnBy(-90)
    forward(s, 5/3)
    k = k + 1

