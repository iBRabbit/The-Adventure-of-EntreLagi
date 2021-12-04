import turtle
import time
import random

# ========= INIT VARIABLES ========= #
DELAY = 0.001 # Delay Kedip Layar
MAX_OBS = 10
MAX_ENEMIES = 2

window = turtle.Screen() # Screen
window.title("Pac-Entre-Lagi")
window.bgcolor("black")
window.setup(width = 600, height = 600)
window.tracer(0)

player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("aqua")
player.penup()
player.goto(0,0)
player.direction = "stop"

obs = [] # Array of Obstacles
enemies = [] # Array of Enemies

# ========= INIT VARIABLES ========= #

# ========= FUNCTIONS ========= #
def initObstacles():
    for i in range(MAX_OBS):
        posx = random.randint(-14, 14) * 20 
        posy = random.randint(-14, 14) * 20
        
        ob = turtle.Turtle()
        ob.speed(0)
        ob.goto(posx, posy)
        ob.penup
        ob.color("green")
        ob.shape("triangle")
        obs.append(ob)

def initEnemies():
    for i in range(MAX_ENEMIES):
        posx = random.randint(-14, 14) * 20 
        posy = random.randint(-14, 14) * 20
        
        en = turtle.Turtle()
        en.speed(0)
        en.goto(posx, posy)
        en.penup
        en.color("red")
        en.shape("circle")
        enemies.append(en)

def getPlayerCurrentPos():
    curr_x = player.xcor()
    curr_y = player.ycor()
    print("[DEBUG] : Player Current Pos -> ", player.pos())
    return curr_x, curr_y

def moveUp():
    getPlayerCurrentPos()
    x = player.xcor()
    y = player.ycor()
    if obstaclesCheck(x, y + 20) == False : return False;
    player.sety(y + 20)

def moveDown():
    getPlayerCurrentPos()
    x = player.xcor()
    y = player.ycor()
    if obstaclesCheck(x, y - 20) == False : return False;
    player.sety(y - 20)

def moveLeft():
    getPlayerCurrentPos()
    x = player.xcor()   
    y = player.ycor()
    if obstaclesCheck(x - 20, y) == False : return False;
    player.setx(x - 20)

def moveRight():
    getPlayerCurrentPos()
    x = player.xcor()
    y = player.ycor()
    if obstaclesCheck(x + 20, y) == False : return False;
    player.setx(x + 20)

def obstaclesCheck(nextX, nextY):
    for i in range(MAX_OBS):
        if nextX == obs[i].xcor() and nextY == obs[i].ycor() : return False
    
    return True

# ========= FUNCTIONS ========= #

def Main():
    initObstacles()
    initEnemies()
    window.listen()
    window.onkey(moveUp, "w")
    window.onkey(moveDown, "s")
    window.onkey(moveLeft, "a")
    window.onkey(moveRight, "d")

    while True:
        window.update()
        time.sleep(DELAY)
        
    window.mainloop()

Main()