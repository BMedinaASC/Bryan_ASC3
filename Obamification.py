from Myro import *

picture = makePicture(pickAFile())
#show(picture)

DarkBlue = makeColor(0,51,76)
Red = makeColor(217, 26, 33)
Blue = makeColor(112,150,158)
Yellow = makeColor(252, 227, 166)

for pixel in getPixels(picture):
    
    gray = getBlue(pixel)
    
    if gray > 180:
        setColor(pixel, Yellow)
        
    elif gray > 120:
        setColor(pixel, Blue)
        
    elif gray > 60:
        setColor(pixel, Red)
        
    else:
        setColor(pixel, DarkBlue)    
        
show(picture)                                                                