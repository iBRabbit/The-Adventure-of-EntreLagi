import turtle
import time
import random
import math

# ========= INIT VARIABLES ========= #
DELAY = 0.001 # Delay Kedip Layar
MAX_OBS = 10
MAX_ENEMIES = 5

window = turtle.Screen() # Screen
window.title("Pac-Entre-Lagi")
window.bgcolor("black")
window.setup(width = 600, height = 600)
window.tracer(0)

player = turtle.Turtle()
player.speed(3)
player.shape("square")
player.color("aqua")
player.penup()
player.goto(0,0)
player.direction = "stop"

goal = turtle.Turtle()
goal.speed()
goal.shape("square")
goal.color("yellow")
goal.penup()
goal.goto(280, -180)


obs = [] # Array of Obstacles
enemies = [] # Array of Enemies

# ========= INIT VARIABLES ========= #

# ========= FUNCTIONS ========= #
 
def distance(x1,y1,x2,y2): # Akhirnya pelajaran kalkulus selama ini kepake
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

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
        en.speed = 1
        en.setposition(posx, posy)
        en.penup()
        en.color("red")
        en.shape("circle")
        en.direction = "stop"
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

def moveEnemy():
    for en in enemies:
        y = en.ycor()
        x = en.xcor()
        
        if distance(player.xcor(), player.ycor(), en.xcor(), en.ycor()) > 200:
            if en.direction == "Up" :
                y += en.speed
                en.direction = "Up"
            elif en.direction == "Down" :
                y += en.speed
                en.direction = "Down"
            continue
        
        distances = {
            "Up" : distance(en.xcor(), en.ycor() + 20, player.xcor(), player.ycor()),
            "Down" : distance(en.xcor(), en.ycor() - 20, player.xcor(), player.ycor()),
            "Left" : distance(en.xcor() + 20, en.ycor(), player.xcor(), player.ycor()),
            "Right" : distance(en.xcor() - 20, en.ycor(), player.xcor(), player.ycor())
        }
        
        mininum = min(distances, key = distances.get)
        
        if mininum == "Up" and distance(en.xcor(), en.ycor() + 20, player.xcor(), player.ycor()) < en.distance(player) : 
            y += en.speed
            en.direction = "Up"
        elif mininum == "Down" and distance(en.xcor(), en.ycor() - 20, player.xcor(), player.ycor()) < en.distance(player) : 
            y += -en.speed
            en.direction = "Down"
        elif mininum == "Left" and distance(en.xcor() + 20, en.ycor(), player.xcor(), player.ycor()) < en.distance(player) : 
            x += en.speed
            en.direction = "Left"
        elif mininum == "Right" and distance(en.xcor() - 20, en.ycor(), player.xcor(), player.ycor()) < en.distance(player) : 
            x += -en.speed
            en.direction = "Right"
        
        # if(distance(en.xcor(), en.ycor() + 20, player.xcor(), player.ycor()) < en.distance(player)): # Go Up
        #     y += en.speed
        # elif(distance(en.xcor(), en.ycor() - 20, player.xcor(), player.ycor()) < en.distance(player)): # Go Down
        #     y += -en.speed
        # elif(distance(en.xcor() + 20, en.ycor(), player.xcor(), player.ycor()) < en.distance(player)): # Go Right
        #     x += en.speed
        # elif(distance(en.xcor() - 20, en.ycor(), player.xcor(), player.ycor()) < en.distance(player)): # Go Left
        #     x += -en.speed
        
        if obstaclesCheck(x,y) == True :
            en.sety(y)
            en.setx(x)
        
        # print(obstaclesCheck(x,y))
    
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
        moveEnemy()
        time.sleep(DELAY)

    window.mainloop()

Main()