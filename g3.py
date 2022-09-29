import pgzrun

WIDTH = 1000
HEIGHT = 500

p = Actor('goat', (100,100))
e = Actor('gorilla', (500,500))


p.speed = 3           #p.speed is variable 
e.speed = 2
gameover = False

def player_movement():
    if keyboard.W:
        p.y -= p.speed
    if keyboard.S:
        p.y += p.speed
    if keyboard.A:
        p.x -= p.speed
    if keyboard.D:
        p.x += p.speed
    #Hanlding the boundary of players
    if p.x < 0:    #if player left side outof screen then enter from right side like snake game 
        p.x = WIDTH
    if p.x > WIDTH:   #vice-versa
        p.x = 0
    if p.y > HEIGHT:
        p.y = 0
    if p.y < 0:
        p.y = HEIGHT

def enemy_movement():
    if p.y > e.y:
        e.y += e.speed
    if p.y <= e.y:
        e.y -= e.speed
    if p.x > e.x:
        e.x += e.speed
    if p.x <= e.x:
        e.x -= e.speed

def check_collision():
    global gameover
    if e.colliderect(p):
        p.image = 'bush4'
        gameover = True

def draw():
    if not gameover:
        screen.clear()
        e.draw()
        p.draw()
    else:
        screen.fill("crimson")
        screen.draw.text("Game over", center = (WIDTH//2, HEIGHT//2) , color = 'white', fontsize = 100)

def update():
    player_movement()
    enemy_movement()
    check_collision()

pgzrun.go()