import pgzrun
from random import randint


WIDTH = 900
HEIGHT = 750

c = Actor('goat',(100,100))
w = Actor('gorilla',(400,400))       #name of actor should be the same as file name of image and initial in small
bush = Actor('bush4', (randint(100,800), randint(100,500)))    ## 100, 800 on x axis       100,500 for y axis 
score = 0   #Global Variable
speed = 5   #Global Variable


def draw():                            #Draw will execute line by line as decalred 
    #screen.fill('purple')
    screen.blit('bg', pos = (0,0))
    c.draw()                               #This will create first character at a layer 
    w.draw()                               #This will create second charcter in upper layer than prev one 
    screen.draw.text("Tekken : Animal Fights",(10,10), color = 'red')
    screen.draw.text(f"Score {score}",(700,10), color = 'black')
    bush.draw()

def update():
    global score
    if keyboard.W:         #WASD should be always capital 
        c.y -= 4
    elif keyboard.S:
        c.y += 4
    elif keyboard.A:
        c.x -= 4
    elif keyboard.D:
        c.x += 4

    if keyboard.up:          
        w.y -= 3
    elif keyboard.down:
        w.y += 3
    elif keyboard.left:
        w.x -= 3
    elif keyboard.right:
        w.x += 3
    
    if c.colliderect(bush):
        score+=1
        bush.pos = (randint(100,800),randint(100,500))

pgzrun.go()