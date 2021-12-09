from operator import setitem, truediv
import turtle
import time
import random
import math

# ========= INIT VARIABLES ========= #
DELAY = 0.001 # Delay Kedip Layar
MAP_SIZE_X = 600
MAP_SIZE_Y = 600
DEFAULT_MAX_OBS = 50
DEFAULT_MAX_ENEMIES = 5
DEFAULT_MAX_FOODS = 3
DEFAULT_MAX_POWERUPS = 3
INVALID_CONSTANT = -99999

level = 1
score = 0
obsQty = DEFAULT_MAX_OBS
enemiesQty = DEFAULT_MAX_ENEMIES
foodsQty = DEFAULT_MAX_FOODS
foodsMaxQty = DEFAULT_MAX_FOODS
powerUpsQty = DEFAULT_MAX_POWERUPS
longDash = 0
timeLD = 0
invincible = 0
timeI = 0
throughTheWall = 0
timeTTW = 0

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

title = turtle.Turtle()
title.speed(0)
title.color("gold")
title.penup()
title.hideturtle()
title.goto(0, 350)
title.write("The Advanture of Entre Lagi", align = "center", font = ("Arial", 30, "normal"))

levelText = turtle.Turtle()
levelText.speed(0)
levelText.color("white")
levelText.penup()
levelText.hideturtle()
levelText.goto(-220, 310)
levelText.write("Level : 1", align = "center", font = ("Arial", 24, "normal"))

scoreText = turtle.Turtle()
scoreText.speed(0)
scoreText.color("white")
scoreText.penup()
scoreText.hideturtle()
scoreText.goto(220,310)
scoreText.write("Score : 0", align = "center", font = ("Arial", 24, "normal"))

gameOverText = turtle.Turtle()
gameOverText.speed(0)
gameOverText.color("white")
gameOverText.penup()
gameOverText.hideturtle()
gameOverText.goto(0,310)

obs = [] # Array of Obstacles
enemies = [] # Array of Enemies
foods = [] # Array of Foods
powerUps = [] # Array of PowerUps

# ========= INIT VARIABLES ========= #

# ========= SETTER ======== #
def setPlayerDirection(direction):
    global player
    player.direction = direction

def setObstaclesQty(obs):
    global obsQty
    obsQty = obs

def setEnemiesQty(enemies):
    global enemiesQty
    enemiesQty = enemies

def setLevel(toLevel):
    global level
    level = toLevel

def setScore(toScore):
    global score
    score = toScore
    
def setFoodQty(foods):
    global foodsQty
    foodsQty = foods
    
def setFoodMaxQty(foods):
    global foodsMaxQty
    foodsMaxQty = foods

def setPowerUpQty(power):
    global powerUpsQty
    powerUpsQty = power

def setLongDash(ld):
    global longDash
    longDash = ld

def setTimeLD(tLD): 
    global timeLD
    timeLD = tLD

def setInvincible(I):
    global invincible
    invincible = I

def setTimeI(tI):    
    global timeI
    timeI = tI
    
def setThroughTheWall(ttw):
    global throughTheWall
    throughTheWall = ttw
    
def setTimeTTW(tTTW):
    global timeTTW
    timeTTW = tTTW

# ========= SETTER ======== #        

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
    line1.penup()
    line1.goto(-300, 300)
    line1.pendown()
    createLine(line1,0)
    line2 = turtle.Turtle()
    line2.fillcolor("red")
    line2.penup()
    line2.goto(300, -300)
    line2.pendown()
    line2.right(180)
    createLine(line2,0)
    line3 = turtle.Turtle()
    line3.fillcolor("red")
    line3.penup()
    line3.goto(300, 295)
    line3.pendown()
    line3.right(90)
    createLine(line3,1)
    line4 = turtle.Turtle()
    line4.fillcolor("red")
    line4.penup()
    line4.goto(-300, -295)
    line4.pendown
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
        ob.speed = 0
        ob.penup()
        ob.goto(posx, posy)
        ob.shape("wall.gif")
        obs.append(ob)

def initEnemies():
    for i in range(enemiesQty):
        check = False
        posx = random.randint(-14, 14) * 20 
        posy = random.randint(-14, 14) * 20
        while not check:
            posx = random.randint(-14, 14) * 20 
            posy = random.randint(-14, 14) * 20
            for j in range(obsQty):
                if not isInRangeOfPoint(posx, posy, obs[j].xcor(), obs[j].ycor(), 10.0):
                    check = True
                else: 
                    check = False
                    break
            if posx >= -280 and posx <= -120 and posy >= -160 and posy <= 160 or posx == 280 and posy == 0: check = False

        en = turtle.Turtle()
        en.speed = 1
        en.penup()
        en.setposition(posx, posy)
        en.shape("enemy.gif")
        direction = random.randint(1,4)
        if direction == 1 : en.direction = "Up"
        elif direction == 2 : en.direction = "Down"
        elif direction == 3 : en.direction = "Left"
        elif direction == 4 : en.direction = "Right"
        enemies.append(en)

def initFoods():
    for i in range(foodsQty):
        check = False
        posx = random.randint(-14, 14) * 20 
        posy = random.randint(-14, 14) * 20
        
        while not check:
            posx = random.randint(-14, 14) * 20 
            posy = random.randint(-14, 14) * 20
            for j in range(obsQty):
                if not isInRangeOfPoint(posx, posy, obs[j].xcor(), obs[j].ycor(), 10.0):
                    check = True
                else: 
                    check = False
                    break
            if not check: continue
            for j in range(enemiesQty):
                if not isInRangeOfPoint(posx, posy, enemies[j].xcor(), enemies[j].ycor(), 10.0):
                    check = True
                else: 
                    check = False
                    break
            if posx == -280 and posy == 0 or posx == 280 and posy == 0: check = False
        food = turtle.Turtle()
        food.speed = 0
        food.penup()
        food.goto(posx, posy)
        food.shape("energy1.gif")
        foods.append(food)

def initPowerUps():
    for i in range(powerUpsQty):
        check = False
        posx = random.randint(-14, 14) * 20 
        posy = random.randint(-14, 14) * 20
        
        while not check:
            posx = random.randint(-14, 14) * 20 
            posy = random.randint(-14, 14) * 20
            for j in range(obsQty):
                if not isInRangeOfPoint(posx, posy, obs[j].xcor(), obs[j].ycor(), 10.0):
                    check = True
                else: 
                    check = False
                    break
            if not check: continue
            for j in range(enemiesQty):
                if not isInRangeOfPoint(posx, posy, enemies[j].xcor(), enemies[j].ycor(), 10.0):
                    check = True
                else: 
                    check = False
                    break
            if not check: continue
            for j in range(foodsQty):
                if not isInRangeOfPoint(posx, posy, foods[j].xcor(), foods[j].ycor(), 10.0):
                    check = True
                else: 
                    check = False
                    break
            if posx == -280 and posy == 0 or posx == 280 and posy == 0: check = False
        power = turtle.Turtle()
        power.speed = 0
        power.penup()
        power.goto(posx, posy)
        power.shape("powerUp.gif")
        power.shapesize(10,10,70)
        powerUps.append(power)

def outOfMapLimit(posx, posy):
    if posx == 300 or posx == -300 or posy == 300 or posy == -300:
        return True
    return False
    
def getPlayerCurrentPos():
    curr_x = player.xcor()
    curr_y = player.ycor()
    # print("[DEBUG] : Player Current Pos -> ", player.pos())
    return curr_x, curr_y

def moveUp():
    x,y = getPlayerCurrentPos()
    if longDash == 1:
        if obstaclesCheck(x, y + 40): return False
        if outOfMapLimit(x, y+40): return False
        player.sety(y + 40)
    else:
        if throughTheWall == 0 and obstaclesCheck(x, y + 20): return False
        if outOfMapLimit(x, y+20): return False
        player.sety(y + 20)
    setPlayerDirection("Up")

def moveDown():
    x,y = getPlayerCurrentPos()
    if longDash == 1:
        if obstaclesCheck(x, y - 40): return False
        if outOfMapLimit(x, y-40): return False
        player.sety(y - 40)
    else:
        if throughTheWall == 0 and obstaclesCheck(x, y - 20) : return False
        if outOfMapLimit(x, y-20): return False
        player.sety(y - 20)
    setPlayerDirection("Down")

def moveLeft():
    x,y = getPlayerCurrentPos()
    if longDash == 1:
        if obstaclesCheck(x - 40, y): return False
        if outOfMapLimit(x-40, y): return False
        player.setx(x - 40)
    else:
        if throughTheWall == 0 and obstaclesCheck(x - 20, y) : return False
        if outOfMapLimit(x-20, y): return False
        player.setx(x - 20)
    setPlayerDirection("Left")

def moveRight():
    x,y = getPlayerCurrentPos()
    if longDash == 1:
        if obstaclesCheck(x + 40, y): return False
        if outOfMapLimit(x+40, y): return False
        player.setx(x + 40)
    else:
        if throughTheWall == 0 and obstaclesCheck(x + 20, y) : return False
        if outOfMapLimit(x+20, y): return False
        player.setx(x + 20)
    setPlayerDirection("Right")

def isInRangeOfPoint(a,b,x,y,radius):
    if a >= x-radius and a <= x+radius and b >= y-radius and b <= y+radius:
        return True 
    return False

def obstaclesCheck(nextX, nextY):
    for i in range(obsQty):
        if isInRangeOfPoint(nextX, nextY, obs[i].xcor(), obs[i].ycor(), 10.0): return True
    return False

def checkEnemyMove(direction, posx, posy):
    if direction == "Up":
        if not obstaclesCheck(posx, posy+1) : return direction
        if distance(player.xcor(), player.ycor(), posx+1, posy) < distance(player.xcor(), player.ycor(), posx-1, posy):
            if not obstaclesCheck(posx+1, posy): return "Right"
            else: return "Left"
        else:
            if not obstaclesCheck(posx-1, posy): return "Left"
            else: return "Right"
    elif direction == "Down":
        if not obstaclesCheck(posx, posy-1) : return direction
        if distance(player.xcor(), player.ycor(), posx+1, posy) < distance(player.xcor(), player.ycor(), posx-1, posy):
            if not obstaclesCheck(posx+1, posy): return "Right"
            else: return "Left"
        else:
            if not obstaclesCheck(posx-1, posy): return "Left"
            else: return "Right"
    elif direction == "Left":
        if not obstaclesCheck(posx-1, posy): return direction
        if distance(player.xcor(), player.ycor(), posx, posy+1) < distance(player.xcor(), player.ycor(), posx, posy-1):
            if not obstaclesCheck(posx, posy+1): return "Up"
            else: return "Down"
        else:
            if not obstaclesCheck(posx, posy-1): return "Down"
            else: return "Up"
    elif direction == "Right":
        if not obstaclesCheck(posx+1, posy): return direction
        if distance(player.xcor(), player.ycor(), posx, posy+1) < distance(player.xcor(), player.ycor(), posx, posy-1):
            if not obstaclesCheck(posx, posy+1): return "Up"
            else: return "Down"
        else:
            if not obstaclesCheck(posx, posy-20): return "Down"
            else: return "Up"

def moveEnemy():
    for en in enemies:
        y = en.ycor()
        x = en.xcor()
        
        if distance(player.xcor(), player.ycor(), en.xcor(), en.ycor()) > 200:
            if en.direction == "Up" :
                if obstaclesCheck(x, y+20):
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
                if obstaclesCheck(x, y-20):
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
                if obstaclesCheck(x-20, y):
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
                if obstaclesCheck(x+20, y):
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
            "Left" : distance(en.xcor() - 20, en.ycor(), player.xcor(), player.ycor()),
            "Right" : distance(en.xcor() + 20, en.ycor(), player.xcor(), player.ycor())
        }

        minimum = min(distances, key = distances.get)
        minimum = checkEnemyMove(minimum, x, y)
        
        if minimum == "Up": #and distance(en.xcor(), en.ycor() + 20, player.xcor(), player.ycor()) < en.distance(player) : 
            y += en.speed
            en.direction = "Up"
        elif minimum == "Down": #and distance(en.xcor(), en.ycor() - 20, player.xcor(), player.ycor()) < en.distance(player) : 
            y += -en.speed
            en.direction = "Down"
        elif minimum == "Left": #and distance(en.xcor() - 20, en.ycor(), player.xcor(), player.ycor()) < en.distance(player) : 
            x += -en.speed
            en.direction = "Left"
        elif minimum == "Right": #and distance(en.xcor() + 20, en.ycor(), player.xcor(), player.ycor()) < en.distance(player) : 
            x += +en.speed
            en.direction = "Right"
          
        en.sety(y)
        en.setx(x)
    
def clearAll():
    for ob in obs:
        ob.goto(INVALID_CONSTANT,INVALID_CONSTANT)
    
    for en in enemies:
        en.goto(INVALID_CONSTANT,INVALID_CONSTANT)
        
    for food in foods:
        food.goto(INVALID_CONSTANT,INVALID_CONSTANT)
    
    for powerUp in powerUps:
        powerUp.goto(INVALID_CONSTANT,INVALID_CONSTANT)

    foods.clear()
    obs.clear()
    enemies.clear()  
    powerUps.clear()   

def setPlayerToSpawn():
    player.setx(-280)
    player.sety(0)
    player.direction = "stop"

def isGoalAchieved():
    if player.distance(goal) < 20.0 and foodsQty <= 0: return True
    else : return False

def clearPowerUps():        
    setTimeLD(0)
    setLongDash(0)
    setTimeI(0)
    setInvincible(0)
    setTimeTTW(0)
    setThroughTheWall(0)
    player.color("aqua")

def goToNextLevel():
    clearAll()
    setPlayerToSpawn()

    setLevel(level + 1)
    updatelevelText()
    
    setObstaclesQty(obsQty + 2)
    initObstacles()

    if level % 4 == 0 : setEnemiesQty(enemiesQty + 1)
    initEnemies()

    setFoodQty(foodsMaxQty + 1)
    setFoodMaxQty(foodsMaxQty + 1)
    initFoods()
    
    clearPowerUps()
    initPowerUps()

def updatelevelText():
    levelText.clear()
    string = "Level : " + str(level) 
    levelText.write(string, align = "center", font = ("Arial", 24, "normal"))

def updateScoreText():
    string = "Score : " + str(score)
    scoreText.clear()
    scoreText.write(string, align = "center", font = ("Arial", 24, "normal"))

def isCollideWithEnemy():
    for en in enemies:
        if isInRangeOfPoint(en.xcor(), en.ycor(), player.xcor(), player.ycor(), 10.0) : return True
    return False

def isCollideWithFood():
    flag = False
    for i in range(foodsQty):
        if longDash == 1:
            x = player.xcor()
            y = player.ycor()

            if player.direction == "Up": y-=20 
            elif player.direction == "Down": y+=20
            elif player.direction == "Left": x+=20
            elif player.direction == "Right": x-=20

            if isInRangeOfPoint(foods[i].xcor(), foods[i].ycor(), x, y, 10.0): flag = True

        elif isInRangeOfPoint(foods[i].xcor(), foods[i].ycor(), player.xcor(), player.ycor(), 10.0): flag = True
        if flag == True:
            foods[i].goto(INVALID_CONSTANT,INVALID_CONSTANT)
            foods.pop(i)
            setFoodQty(foodsQty - 1)
            return True
    return False        

def isCollideWithPowerUp():
    for i in range(powerUpsQty):
        if isInRangeOfPoint(powerUps[i].xcor(), powerUps[i].ycor(), player.xcor(), player.ycor(), 10.0):
            powerUps[i].goto(INVALID_CONSTANT,INVALID_CONSTANT)
            return i
    return -1

def getPowerUp(PU):
    clearPowerUps()
    if PU == 0:
        setLongDash(1)
        setTimeLD(500)
        player.color("purple")
    elif PU == 1:
        setInvincible(1)
        setTimeI(500)
        player.color("grey")
    elif PU == 2:
        setThroughTheWall(1)
        setTimeTTW(500)
        player.color("white")

def timeLongDash():
    setTimeLD(timeLD - 1)
    if(timeLD <= 0): 
        setLongDash(0)
        setTimeLD(0)
        player.color("blue")

def timeInvincible():
    setTimeI(timeI - 1)
    if(timeI <= 0): 
        setInvincible(0)
        setTimeI(0)
        player.color("blue")

def timeThroughTheWall():
    setTimeTTW(timeTTW - 1)
    if(timeTTW <= 0): 
        setThroughTheWall(0)
        setTimeTTW(0)
        player.color("blue")

def gameOver():
    setLevel(1)
    setScore(0)
    updatelevelText()
    updateScoreText()
    clearAll()
    setPlayerToSpawn()
    setObstaclesQty(DEFAULT_MAX_OBS)
    setEnemiesQty(DEFAULT_MAX_ENEMIES)
    setFoodQty(DEFAULT_MAX_FOODS)
    initObstacles()
    initEnemies()
    initFoods()
    clearPowerUps()
    initPowerUps()
    gameOverText.write("GAME OVER", align = "center", font = ("Arial", 24, "normal"))
    time.sleep(3)
    gameOverText.clear()

def registerShape():
    turtle.register_shape("powerUp.gif")
    turtle.register_shape("wall.gif")
    turtle.register_shape("enemy.gif")
    turtle.register_shape("energy1.gif")

# ========= FUNCTIONS ========= #

if __name__ == "__main__":
    registerShape()
    border()
    initObstacles()
    initEnemies()
    initFoods()
    initPowerUps()
    window.listen()
    window.onkey(moveUp, "w")
    window.onkey(moveDown, "s")
    window.onkey(moveLeft, "a")
    window.onkey(moveRight, "d")
    # x = 5
    while True:
        window.update()
        moveEnemy()
        if isGoalAchieved() : goToNextLevel()
        if isCollideWithEnemy() and invincible == 0: gameOver()
        if isCollideWithFood():
            setScore(score + 10)
            updateScoreText()
        PU = isCollideWithPowerUp()
        if PU != -1: 
            getPowerUp(PU)
            PU = -1
        if timeLD > 0.0:
            timeLongDash()
        if timeI > 0.0:
            timeInvincible()
        if timeTTW > 0.0:
            timeThroughTheWall()
        time.sleep(DELAY)

    window.mainloop()