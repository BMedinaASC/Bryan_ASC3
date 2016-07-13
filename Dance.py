from Myro import *

s = 1

i = 0
while i < 2:
    turnBy(180)
    i = i + 1

forward(s, 1.4)
backward(s, 1.4)
turnBy(80)
forward(s, 1.2)

turnLeft(s, 1.9)
turnLeft(s, 2.1)
    
backward(s, 1.4)