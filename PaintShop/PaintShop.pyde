Color = color(0, 0, 0)

def setup():
    size(400, 400)
    background(255, 255, 255)
    
def draw():
    noStroke()
    fill(255, 0, 0)
    rect(0, 0, 50, 50)
    noStroke()
    fill(0, 255, 0)  
    rect(50, 0, 50, 50)
    noStroke()
    fill(0, 0, 255)
    rect(100, 0, 50, 50)
    noStroke()
    fill(255, 255, 0)
    rect(150, 0, 50, 50)
    noStroke()
    fill(0, 255, 255)
    rect(200, 0, 50, 50)
    noStroke()
    fill(255, 0, 255)
    rect(250, 0, 50, 50)
    noStroke()
    fill(0, 0, 0)
    rect(300, 0, 50, 50)
    noStroke()
    fill(255, 255, 255)
    rect(350, 0, 50, 50)
    
    x = mouseX
    y = mouseY
    
    global Color
    
    if mouseY < 50:
        if mousePressed and (mouseButton == LEFT):
            if mouseX > 0 and mouseX < 50:
                Color = color(255, 0, 0)
            elif mouseX > 50 and mouseX < 100:
                Color = color(0, 255, 0)
            elif mouseX > 100 and mouseX < 150:
                Color = color(0, 0, 255)
            elif mouseX > 150 and mouseX < 200:
                Color = color(255, 255, 0)
            elif mouseX > 200 and mouseX < 250:
                Color = color(0, 255, 255)
            elif mouseX > 250 and mouseX < 300:
                Color = color(255, 0, 255)
            elif mouseX > 300 and mouseX < 350:
                Color = color(0, 0, 0)
            elif mouseX > 350 and mouseX < 400:
                Color = color(255, 255, 255)
            
    else:
        if mousePressed and (mouseButton == LEFT):
            if Color == color (255, 255, 255):
                noStroke()
                fill(Color)
                rect(x, y, 20, 20)
            else:
                noStroke()
                fill (Color)
                ellipse(x, y, 5, 5)