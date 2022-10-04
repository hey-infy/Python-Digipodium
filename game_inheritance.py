from random import randint as ri
import pgzrun

WIDTH = 800
HEIGHT = 500

#All the class logic for a player 
class Player(Actor):
    #Overriding the default constructor
    def __init__(self, image, speed = 2):
        pos = ri(0, WIDTH), ri(0, HEIGHT)   #generate randon x y positional cordinate for player
        super().__init__(image, pos)    #call the parent class constructor and pass image and pos
        self.speed = speed    #Add a new instance variable

    
    def move(self):
        if keyboard.W:
            self.y -= self.speed
        elif keyboard.S:
            self.y += self.speed
        elif keyboard.A:
            self.x -= self.speed
            self.angle = +10
        elif keyboard.D:
            self.x += self.speed
            self.angle = -10
        elif keyboard.E:
            self.x += self.speed
            self.y -= self.speed
            self.angle = -10
        elif keyboard.Q:
            self.x -= self.speed
            self.y -= self.speed
            self.angle = +10
        elif keyboard.Z:
            self.x -= self.speed
            self.y += self.speed
            self.angle = +10
        elif keyboard.X:
            self.x += self.speed
            self.y += self.speed
            self.angle = -10
        else:
            self.angle = 0

    def check_boundary(self):
        if self.x < 0:    #if player left side outof screen then enter from right side like snake game 
            self.x = WIDTH
        if self.x > WIDTH:   #vice-versa
            self.x = 0
        if self.y > HEIGHT:
            self.y = 0
        if self.y < 0:
            self.y = HEIGHT


#Main Game code 
p = Player('ironman')

def draw():
    screen.fill('black')
    p.draw()

def update():
    p.move()
    p.check_boundary()

pgzrun.go()
