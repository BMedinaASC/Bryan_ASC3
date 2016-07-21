SpaceX = 280
invaders = []
for i in range(11):
    invaders.append([0]*5)

def setup():
    size(1280, 720)
    frameRate(120)
    
def keyPressed():
    global SpaceX
    if key == "a":
        SpaceX = SpaceX - 10
    if key == "d":
        SpaceX = SpaceX + 10

def draw():
    global SpaceX
    
    background(255, 255, 255)
    
    #Spaceship Body
    fill(255, 255, 255)
    rect(SpaceX, 660, 60, 15, 40, 40, 0, 0)
    
    #Spaceship Cockpit
    fill(0, 255, 255)
    rect(SpaceX + 23.25, 640, 15, 20, 10, 10, 0, 0)
    
    #Spaceship Engines
    fill(255, 0, 0)
    rect(SpaceX + 10, 670, 8, 15)
    rect(SpaceX + 40, 670, 8, 15)