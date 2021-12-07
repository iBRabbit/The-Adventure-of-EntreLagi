import turtle
import time
import random
import math

# ========= INIT VARIABLES ========= #
DELAY = 0.1 # Delay Kedip Layar
MAP_SIZE_X = 600
MAP_SIZE_Y = 600

level = 1
obsQty = 50
enemiesQty = 5

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
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, 310)
text.write("Level : 1", align = "center", font = ("Arial", 24, "normal"))

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
    for i in range(obsQty):
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
    for i in range(enemiesQty):
        check = False
        while check == False:
            posx = random.randint(-14, 14) * 20 
            posy = random.randint(-14, 14) * 20
            for j in range(obsQty):
                if abs(posx - obs[j].xcor()) >= 20 and abs(posy - obs[j].ycor()) >= 20:
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
    x,y = getPlayerCurrentPos()
    if obstaclesCheck(x, y + 20) == False : return False
    if mapLimit(x, y+20) == True: return False
    player.sety(y + 20)

def moveDown():
    x,y = getPlayerCurrentPos()
    if obstaclesCheck(x, y - 20) == False : return False
    if mapLimit(x, y-20) == True: return False
    player.sety(y - 20)

def moveLeft():
    x,y = getPlayerCurrentPos()
    if obstaclesCheck(x - 20, y) == False : return False
    if mapLimit(x-20, y) == True: return False
    player.setx(x - 20)

def moveRight():
    x,y = getPlayerCurrentPos()
    if obstaclesCheck(x + 20, y) == False : return False
    if mapLimit(x+20, y) == True: return False
    player.setx(x + 20)

def isInRangeOfPoint(a,b,x,y,radius):
    if a >= x-radius and a <= x+radius and b >= y-radius and b <= y+radius:
        return True 
    return False

def obstaclesCheck(nextX, nextY):
    '''
    Kalo True -> Ga Ada Obstacle
    Kalo False -> Ada obstacle
    '''
    for i in range(obsQty):
        if isInRangeOfPoint(obs[i].xcor(), obs[i].ycor(), nextX, nextY, 10) == True: return False
    return True

def checkEnemyMove(direction, posx, posy):
    if direction == "Up" or direction == "Down":
        if direction == "Up" and obstaclesCheck(posx, posy+20) == True: return direction
        elif direction == "Down" and obstaclesCheck(posx, posy-20) == True: return direction
        elif obstaclesCheck(posx+20, posy) == True and obstaclesCheck(posx-20, posy) == False: return "Right"
        elif obstaclesCheck(posx+20, posy) == False and obstaclesCheck(posx-20, posy) == True: return "Left"
        elif obstaclesCheck(posx+20, posy) == True and obstaclesCheck(posx-20, posy) == True: 
            if distance(player.xcor(), player.ycor(), posx+20, posy) < distance(player.xcor(), player.ycor(), posx-20, posy): 
                return "Right"
            else: return "Left"
    elif direction == "Left" or direction == "Right":
        if direction == "Left" and obstaclesCheck(posx-20, posy) == True: return direction
        elif direction == "Right" and obstaclesCheck(posx+20, posy) == True: return direction
        elif obstaclesCheck(posx, posy+20) == True and obstaclesCheck(posx, posy-20) == False: return "Up"
        elif obstaclesCheck(posx, posy+20) == False and obstaclesCheck(posx, posy-20) == True: return "Down"
        elif obstaclesCheck(posx, posy+20) == True and obstaclesCheck(posx, posy-20) == True: 
            if distance(player.xcor(), player.ycor(), posx, posy+20) < distance(player.xcor(), player.ycor(), posx, posy-20): 
                return "Up"
            else: return "Down"

def moveEnemy():
    for en in enemies:
        y = en.ycor()
        x = en.xcor()
        
        if distance(player.xcor(), player.ycor(), en.xcor(), en.ycor()) > 200:
            if en.direction == "Up" :
                if obstaclesCheck(x, y+20) == False:
                    y -= en.speed
                    en.direction = "Down"
                else: 
                    if y > 280: 
                        en.direction = "Down"
                        y -= en.speed
                    else: 
                        en.direction = "Up"
                        y += en.speed
            elif en.direction == "Down" :
                if obstaclesCheck(x, y-20) == False:
                    y += en.speed
                    en.direction = "Up"
                else:
                    if y < -280: 
                        en.direction = "Up"
                        y += en.speed
                    else: 
                        en.direction = "Down"
                        y -= en.speed
            elif en.direction == "Left" :
                if obstaclesCheck(x-20, y) == False:
                    x += en.speed
                    en.direction = "Right"
                else:
                    if x < -280: 
                        en.direction = "Right"
                        x += en.speed
                    else: 
                        en.direction = "Left"
                        x -= en.speed
            elif en.direction == "Right" :
                if obstaclesCheck(x+20, y) == False:
                    x -= en.speed
                    en.direction = "Left"
                else:
                    if x > 280: 
                        en.direction = "Left"
                        x -= en.speed
                    else: 
                        en.direction = "Right"
                        x += en.speed
            en.sety(y)
            en.setx(x)
            continue
        
        distances = {
            "Up" : distance(en.xcor(), en.ycor() + 20, player.xcor(), player.ycor()),
            "Down" : distance(en.xcor(), en.ycor() - 20, player.xcor(), player.ycor()),
            "Left" : distance(en.xcor() + 20, en.ycor(), player.xcor(), player.ycor()),
            "Right" : distance(en.xcor() - 20, en.ycor(), player.xcor(), player.ycor())
        }

        minimum = min(distances, key = distances.get)
        minimum = checkEnemyMove(minimum, x, y)
        
        if minimum == "Up" and distance(en.xcor(), en.ycor() + 20, player.xcor(), player.ycor()) < en.distance(player) : 
            y += en.speed
            en.direction = "Up"
        elif minimum == "Down" and distance(en.xcor(), en.ycor() - 20, player.xcor(), player.ycor()) < en.distance(player) : 
            y += -en.speed
            en.direction = "Down"
        elif minimum == "Left" and distance(en.xcor() + 20, en.ycor(), player.xcor(), player.ycor()) < en.distance(player) : 
            x += en.speed
            en.direction = "Left"
        elif minimum == "Right" and distance(en.xcor() - 20, en.ycor(), player.xcor(), player.ycor()) < en.distance(player) : 
            x += -en.speed
            en.direction = "Right"
          
        en.sety(y)
        en.setx(x)
    
def clearAll():
    for i in range(obsQty):
        obs[i].reset()
    
    for i in range(enemiesQty):
        enemies[i].reset()
        
    
def setPlayerToSpawn():
    player.setx(-280)
    player.sety(0)
    player.direction = "stop"

def isGoalAchieved():
    if player.distance(goal) < 20.0 : return True
    else : return False
        
def setLevel(toLevel):
    global level
    level = toLevel
        
def goToNextLevel():
    clearAll()
    setPlayerToSpawn()
    initObstacles()
    initEnemies()
    
    currLevel = level
    setLevel(currLevel + 1)
    
    currObs = obsQty
    currEnemies = enemiesQty
    
    if level % 2 == 0 : 
        currObs += 10
        setObstacles(currObs)
    
    if level % 2 == 1 :
        currEnemies += 1
        setEnemiesQty(currEnemies)
       
def setObstacles(obs):
    global obsQty
    obsQty = obs

def setEnemiesQty(enemies):
    global enemiesQty
    enemiesQty = enemies
        
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
    # x = 5
    while True:
        window.update()
        moveEnemy()
        if isGoalAchieved() == True : goToNextLevel()
        time.sleep(0.1)

    window.mainloop()

if __name__ == "__main__":
    Main()