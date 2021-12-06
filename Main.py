import turtle
import time
import random
import math

# ========= INIT VARIABLES ========= #
DELAY = 0.1 # Delay Kedip Layar
MAX_OBS = 100
MAX_ENEMIES = 5

window = turtle.Screen() # Screen
window.title("Pac-Entre-Lagi")
window.bgcolor("black")
window.setup(width = 800, height = 800)
window.tracer(0)

player = turtle.Turtle()
player.speed(3)
player.shape("square")
player.color("aqua")
player.penup()
player.goto(-280, 0)
player.direction = "stop"

goal = turtle.Turtle()
goal.speed()
goal.shape("square")
goal.color("yellow")
goal.penup()
goal.goto(280, 0)

text = turtle.Turtle()
text.speed(0)
# text.shape("line")
text.color("white")
text.penup()
text.hideturtle()
# text.


obs = [] # Array of Obstacles
enemies = [] # Array of Enemies

# ========= INIT VARIABLES ========= #

# ========= FUNCTIONS ========= #
 
def createLine(line, x):
    if x == 0:
        line.begin_fill()
        line.forward(600)
        line.right(90)
        line.forward(5)
        line.right(90)
        line.forward(600)
        line.hideturtle()
        line.end_fill()
    if x == 1:
        line.begin_fill()
        line.forward(590)
        line.right(90)
        line.forward(5)
        line.right(90)
        line.forward(590)
        line.hideturtle()
        line.end_fill()

def border():
    line1 = turtle.Turtle()
    line1.fillcolor("red")
    line1.goto(-300, 300)
    createLine(line1,0)
    line2 = turtle.Turtle()
    line2.fillcolor("red")
    line2.goto(300, -300)
    line2.right(180)
    createLine(line2,0)
    line3 = turtle.Turtle()
    line3.fillcolor("red")
    line3.goto(300, 295)
    line3.right(90)
    createLine(line3,1)
    line4 = turtle.Turtle()
    line4.fillcolor("red")
    line4.goto(-300, -295)
    line4.left(90)
    createLine(line4,1)

def distance(x1,y1,x2,y2): # Akhirnya pelajaran kalkulus selama ini kepake
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def initObstacles():
    for i in range(MAX_OBS):
        posx = random.randint(-14, 14) * 20 
        posy = random.randint(-14, 14) * 20
        
        while posx == -280 and posy == 0 or posx == 280 and posy == 0:
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
        check = False
        while check == False:
            posx = random.randint(-14, 14) * 20 
            posy = random.randint(-14, 14) * 20
            for j in range(MAX_OBS):
                if posx != obs[j].xcor() and posy != obs[j].ycor():
                    check = True
                    break
            if check == True: break

        en = turtle.Turtle()
        en.speed = 5
        en.setposition(posx, posy)
        en.penup()
        en.color("red")
        en.shape("circle")
        direction = random.randint(1,4)
        if direction == 1 : en.direction = "Up"
        elif direction == 2 : en.direction = "Down"
        elif direction == 3 : en.direction = "Left"
        elif direction == 4 : en.direction = "Right"
        enemies.append(en)

def mapLimit(posx, posy):
    if posx == 300 or posx == -300 or posy == 300 or posy == -300:
        return True
    return False
    
def getPlayerCurrentPos():
    curr_x = player.xcor()
    curr_y = player.ycor()
    print("[DEBUG] : Player Current Pos -> ", player.pos())
    return curr_x, curr_y

def moveUp():
    getPlayerCurrentPos()
    x = player.xcor()
    y = player.ycor()
    if obstaclesCheck(x, y + 20) == False : return False
    if mapLimit(x, y+20) == True: return False
    player.sety(y + 20)

def moveDown():
    getPlayerCurrentPos()
    x = player.xcor()
    y = player.ycor()
    if obstaclesCheck(x, y - 20) == False : return False
    if mapLimit(x, y-20) == True: return False
    player.sety(y - 20)

def moveLeft():
    getPlayerCurrentPos()
    x = player.xcor()   
    y = player.ycor()
    if obstaclesCheck(x - 20, y) == False : return False
    if mapLimit(x-20, y) == True: return False
    player.setx(x - 20)

def moveRight():
    getPlayerCurrentPos()
    x = player.xcor()
    y = player.ycor()
    if obstaclesCheck(x + 20, y) == False : return False
    if mapLimit(x+20, y) == True: return False
    player.setx(x + 20)

def obstaclesCheck(nextX, nextY):
    for i in range(MAX_OBS):
        if abs(nextX - obs[i].xcor()) < 20  and abs(nextY - obs[i].ycor()) < 20 : return False
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
                y -= en.speed
                en.direction = "Down"
            elif en.direction == "Left" :
                x += en.speed
                en.direction = "Left"
            elif en.direction == "Right" :
                x -= en.speed
                en.direction = "Right"
            if obstaclesCheck(x, y) == False : continue
            en.sety(y)
            en.setx(x)
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
        
        if obstaclesCheck(x,y) == False :
            x
        else :     
            en.sety(y)
            en.setx(x)
        
        # print(obstaclesCheck(x,y))
    
# ========= FUNCTIONS ========= #

def Main():
    border()
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