from operator import setitem, truediv
import turtle
import time
import random
import math
import winsound
# from playsound import playsound

# ========= INIT VARIABLES ========= #
DELAY = 0.001 # Delay Kedip Layar
MAP_SIZE_X = 600
MAP_SIZE_Y = 600
DEFAULT_MAX_OBS = 50
DEFAULT_MAX_ENEMIES = 5
DEFAULT_MAX_FOODS = 3
DEFAULT_MAX_POWERUPS = 4
INVALID_CONSTANT = -99999

numPlayer = 1
alivePlayer = 2
level = 1
score = 0
obsQty = DEFAULT_MAX_OBS
enemiesQty = DEFAULT_MAX_ENEMIES
foodsQty = DEFAULT_MAX_FOODS
foodsMaxQty = DEFAULT_MAX_FOODS
powerUpsQty = DEFAULT_MAX_POWERUPS
highScore = 0
longDash = 0
invincible = 0
throughTheWall = 0
reversedMove = 0
PUTime = 0
PUType = -1
isPaused = False

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
player2 = turtle.Turtle()

goal = turtle.Turtle()
goal.speed()
goal.shape("square")
goal.color("yellow")
goal.penup()
goal.goto(280, 0)

title = turtle.Turtle()
levelText = turtle.Turtle()
scoreText = turtle.Turtle()

gameOverText = turtle.Turtle()
gameOverText.speed(0)
gameOverText.color("red")
gameOverText.penup()
gameOverText.hideturtle()
gameOverText.goto(0, -340)

power = turtle.Turtle()
power.speed(0)
power.color("red")
power.penup()
power.hideturtle()
power.goto(0,-340)

obs = [] # Array of Obstacles
enemies = [] # Array of Enemies
foods = [] # Array of Foods
powerUps = [] # Array of PowerUps
typePower = ["Long Dash ", "Invincible ", "Through The Wall ", "Reverse "]

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
    
def setInvincible(I):
    global invincible
    invincible = I

def setThroughTheWall(ttw):
    global throughTheWall
    throughTheWall = ttw

def setPUTime(time):
    global PUTime
    PUTime = time
    
def setHighScore(toScore):
    global highScore
    highScore = toScore
    saveHighScore()

def setPUType(typeP):
    global PUType
    PUType = typeP

def setPaused(params):
    global isPaused
    isPaused = params
    
def setAlivePlayer(alive):
    global alivePlayer
    alivePlayer = alive
    
# ========= SETTER ======== #        

# ========= FUNCTIONS ========= #

def createText():
    title.speed(0)
    title.color("gold")
    title.penup()
    title.hideturtle()
    title.goto(0, 350)
    title.write("The Advanture of Entre Lagi", align = "center", font = ("Arial", 30, "normal"))

    levelText.speed(0)
    levelText.color("white")
    levelText.penup()
    levelText.hideturtle()
    levelText.goto(-240, 310)
    levelText.write("Level : 1", align = "center", font = ("Arial", 24, "normal"))

    scoreText.speed(0)
    scoreText.color("white")
    scoreText.penup()
    scoreText.hideturtle()
    scoreText.goto(110,310)
    scoreText.write("Score : 0 High Score : 0", align = "center", font = ("Arial", 24, "normal"))

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

def initPlayer2():
    player2.showturtle()
    player2.speed(3)
    player2.shape("circle")
    player2.color("aqua")
    player2.penup()
    player2.goto(-280, 0)
    player2.direction = "stop"

def initObstacles():
    for i in range(obsQty):
        check = False
        posx = random.randint(-14, 14) * 20 
        posy = random.randint(-14, 14) * 20
        while not check:
            posx = random.randint(-14, 14) * 20 
            posy = random.randint(-14, 14) * 20
            if (posx == -280 and posy == 0) or (posx == 280 and posy == 0) or (posx == -280 and posy == 20) or (posx == -280 and posy == -20): check = False
            else: check = True
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
        food.shape("energy.gif")
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
        powers = turtle.Turtle()
        powers.speed = 0
        powers.penup()
        powers.goto(posx, posy)
        powers.shape("powerUp.gif")
        powers.shapesize(10,10,70)
        powerUps.append(powers)

def outOfMapLimit(posx, posy):
    if posx >= 300 or posx <= -300 or posy >= 300 or posy <= -300:
        return True
    return False
    
def getPlayerCurrentPos(nPlayer):
    if nPlayer == 1:
        curr_x = player.xcor()
        curr_y = player.ycor()
    else:
        curr_x = player2.xcor()
        curr_y = player2.ycor()
    return curr_x, curr_y

def moveUp(reverseCheck, nPlayer):
    x,y = getPlayerCurrentPos(nPlayer)
    
    if isPaused : return 1
    if reversedMove == 1 and reverseCheck == True: return moveDown(False, nPlayer)

    if longDash == 1:
        if obstaclesCheck(x, y + 40): return False
        if outOfMapLimit(x, y+40): return False
        if nPlayer == 2 : player2.sety(y + 40)
        else : player.sety(y + 40)
    else:
        if throughTheWall == 0 and obstaclesCheck(x, y + 20): return False
        if outOfMapLimit(x, y+20): return False
        if nPlayer == 2 : player2.sety(y + 20)
        else : player.sety(y + 20)
    setPlayerDirection("Up")

def moveDown(reverseCheck, nPlayer):
    x,y = getPlayerCurrentPos(nPlayer)
    
    if isPaused : return 1
    if reversedMove == 1 and reverseCheck == True: return moveUp(False, nPlayer)
    
    if longDash == 1:
        if obstaclesCheck(x, y - 40): return False
        if outOfMapLimit(x, y-40): return False
        if nPlayer == 2 : player2.sety(y - 40)
        else : player.sety(y - 40)
    else:
        if throughTheWall == 0 and obstaclesCheck(x, y - 20) : return False
        if outOfMapLimit(x, y-20): return False
        if nPlayer == 2 : player2.sety(y - 20)
        else : player.sety(y - 20)
    setPlayerDirection("Down")

def moveLeft(reverseCheck, nPlayer):
    x,y = getPlayerCurrentPos(nPlayer)
    
    if isPaused : return 1
    if reversedMove == 1 and reverseCheck == True : return moveRight(False, nPlayer)
    
    if longDash == 1:
        if obstaclesCheck(x - 40, y): return False
        if outOfMapLimit(x-40, y): return False
        if nPlayer == 2 : player2.setx(x - 40)
        else : player.setx(x - 40)
    else:
        if throughTheWall == 0 and obstaclesCheck(x - 20, y) : return False
        if outOfMapLimit(x-20, y): return False
        if nPlayer == 2 : player2.setx(x - 20)
        else : player.setx(x - 20)
    setPlayerDirection("Left")

def moveRight(reverseCheck, nPlayer):
    x,y = getPlayerCurrentPos(nPlayer)
    
    if isPaused : return 1
    if reversedMove == 1 and reverseCheck == True: return moveLeft(False, nPlayer)
    
    if longDash == 1:
        if obstaclesCheck(x + 40, y): return False
        if outOfMapLimit(x+40, y): return False
        if nPlayer == 2 : player2.setx(x + 40)
        else : player.setx(x + 40)
    else:
        if throughTheWall == 0 and obstaclesCheck(x + 20, y) : return False
        if outOfMapLimit(x+20, y): return False
        if nPlayer == 2 : player2.setx(x + 20)
        else : player.setx(x + 20)
    setPlayerDirection("Right")

def mUp():
    moveUp(True, 1)

def mDown():
    moveDown(True, 1)

def mLeft():
    moveLeft(True, 1)

def mRight():
    moveRight(True, 1)

def mUp2():
    moveUp(True, 2)

def mDown2():
    moveDown(True, 2)

def mLeft2():
    moveLeft(True, 2)

def mRight2():
    moveRight(True, 2)

def isInRangeOfPoint(a,b,x,y,radius):
    if a >= x-radius and a <= x+radius and b >= y-radius and b <= y+radius:
        return True 
    return False

def obstaclesCheck(nextX, nextY):
    for i in range(obsQty):
        if isInRangeOfPoint(nextX, nextY, obs[i].xcor(), obs[i].ycor(), 10.0): return True
    return False

def checkEnemyMove(enemy_direc, direction, posx, posy): #knowledgeBase
    if direction == "Up":
        if enemy_direc != "Down" and not obstaclesCheck(posx, posy+1) : return direction
        elif obstaclesCheck(posx+1, posy) and obstaclesCheck(posx-1, posy): return "Down"
        elif distance(player.xcor(), player.ycor(), posx+1, posy) <= distance(player.xcor(), player.ycor(), posx-1, posy):
            if enemy_direc != "Left" and not obstaclesCheck(posx+1, posy): return "Right"
            elif enemy_direc != "Right" and not obstaclesCheck(posx-1, posy): return "Left"
            else: return "Down"
        else:
            if enemy_direc != "Right" and not obstaclesCheck(posx-1, posy): return "Left"
            elif enemy_direc != "Left" and not obstaclesCheck(posx+1, posy): return "Right"
            else: return "Down"
    elif direction == "Down":
        if enemy_direc != "Up" and not obstaclesCheck(posx, posy-1) : return direction
        elif obstaclesCheck(posx+1, posy) and obstaclesCheck(posx-1, posy): return "Up"
        elif distance(player.xcor(), player.ycor(), posx+1, posy) <= distance(player.xcor(), player.ycor(), posx-1, posy):
            if enemy_direc != "Left" and not obstaclesCheck(posx+1, posy): return "Right"
            elif enemy_direc != "Right" and not obstaclesCheck(posx-1, posy): return "Left"
            else: return "Up"
        else:
            if enemy_direc != "Right" and not obstaclesCheck(posx-1, posy): return "Left"
            elif enemy_direc != "Left" and not obstaclesCheck(posx+1, posy): return "Right"
            else: return "Up"
    elif direction == "Left":
        if enemy_direc != "Right" and not obstaclesCheck(posx-1, posy): return direction
        elif obstaclesCheck(posx, posy+1) and obstaclesCheck(posx, posy-1): return "Right"
        elif distance(player.xcor(), player.ycor(), posx, posy+1) <= distance(player.xcor(), player.ycor(), posx, posy-1):
            if enemy_direc != "Down" and not obstaclesCheck(posx, posy+1): return "Up"
            elif enemy_direc != "Up" and not obstaclesCheck(posx, posy-1): return "Down"
            else: return "Right"
        else:
            if enemy_direc != "Up" and not obstaclesCheck(posx, posy-1): return "Down"
            elif enemy_direc != "Down" and not obstaclesCheck(posx, posy+1): return "Up"
            else: return "Right"
    elif direction == "Right":
        if enemy_direc != "Left" and not obstaclesCheck(posx+1, posy): return direction
        elif obstaclesCheck(posx, posy+1) and obstaclesCheck(posx, posy-1): return "Left"
        elif distance(player.xcor(), player.ycor(), posx, posy+1) <= distance(player.xcor(), player.ycor(), posx, posy-1):
            if enemy_direc != "Down" and not obstaclesCheck(posx, posy+1): return "Up"
            elif enemy_direc != "Up" and not obstaclesCheck(posx, posy-20): return "Down"
            else: return "Left"
        else:
            if enemy_direc != "Up" and not obstaclesCheck(posx, posy-20): return "Down"
            elif enemy_direc != "Down" and not obstaclesCheck(posx, posy+1): return "Up"
            else: return "Left"

def moveEnemy():
    for en in enemies:
        y = en.ycor()
        x = en.xcor()
        
        if distance(player.xcor(), player.ycor(), en.xcor(), en.ycor()) > 200 and distance(player2.xcor(), player2.ycor(), en.xcor(), en.ycor()) > 200:
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
        if numPlayer == 1:
            distances = {
                "Up" : distance(en.xcor(), en.ycor() + 20, player.xcor(), player.ycor()),
                "Down" : distance(en.xcor(), en.ycor() - 20, player.xcor(), player.ycor()),
                "Left" : distance(en.xcor() - 20, en.ycor(), player.xcor(), player.ycor()),
                "Right" : distance(en.xcor() + 20, en.ycor(), player.xcor(), player.ycor())
            }
        else:
            distances = {
                "Up" : min(distance(en.xcor(), en.ycor() + 20, player.xcor(), player.ycor()), distance(en.xcor(), en.ycor() + 20, player2.xcor(), player2.ycor())),
                "Down" : min(distance(en.xcor(), en.ycor() - 20, player.xcor(), player.ycor()), distance(en.xcor(), en.ycor() - 20, player2.xcor(), player2.ycor())),
                "Left" : min(distance(en.xcor() - 20, en.ycor(), player.xcor(), player.ycor()), distance(en.xcor() - 20, en.ycor(), player2.xcor(), player2.ycor())),
                "Right" : min(distance(en.xcor() + 20, en.ycor(), player.xcor(), player.ycor()), distance(en.xcor() + 20, en.ycor(), player2.xcor(), player2.ycor()))
            }

        minimum = min(distances, key = distances.get)
        minimum = checkEnemyMove(en.direction, minimum, x, y)

        if minimum == "Up": 
            y += en.speed
            en.direction = "Up"
        elif minimum == "Down": 
            y -= en.speed
            en.direction = "Down"
        elif minimum == "Left": 
            x -= en.speed
            en.direction = "Left"
        elif minimum == "Right":
            x += en.speed
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
    power.clear()   

def setPlayerToSpawn():
    player.setx(-280)
    player.sety(0)
    player.direction = "stop"
    if numPlayer == 2:
        player2.setx(-280)
        player2.sety(0)
        player2.direction = "stop"

def isGoalAchieved():
    if numPlayer == 1 :
        if player.distance(goal) < 20.0 and foodsQty <= 0 : return True
        else : return False
    else :
        if player.distance(goal) < 20.0 and player2.distance(goal) < 20.0 and foodsQty <= 0 : return True 
        elif alivePlayer == 1 and foodsQty <= 0 : 
            if player.distance(goal) < 20.0 : return True
            if player2.distance(goal) < 20.0 : return True
        else:
            if player.distance(goal) < 20.0 and foodsQty <= 0 :
                player.goto(-INVALID_CONSTANT,INVALID_CONSTANT)
                setAlivePlayer(alivePlayer-1)
            if player2.distance(goal) < 20.0 and foodsQty <= 0 :
                player2.goto(-INVALID_CONSTANT,INVALID_CONSTANT)
                setAlivePlayer(alivePlayer-1)
            return False

def clearPowerUps():
    setPUTime(0)
    setLongDash(0)
    setInvincible(0)
    setReverse(0)
    setThroughTheWall(0)
    player.color("aqua")
    player2.color("aqua")

def goToNextLevel():
    clearAll()
    setPlayerToSpawn()

    setLevel(level + 1)
    updatelevelText()
    
    if numPlayer == 1 : setObstaclesQty(obsQty + 40)
    else : setObstaclesQty(obsQty + 30)
    initObstacles()

    winsound.PlaySound("mixkit-arcade-game-complete-or-approved-mission-205.wav", winsound.SND_ASYNC)

    if level % 4 == 0 and numPlayer == 1 : setEnemiesQty(enemiesQty + 1)
    else : setEnemiesQty(enemiesQty + 2)
    initEnemies()

    if numPlayer == 1 : 
        setFoodQty(foodsMaxQty + 1)
        setFoodMaxQty(foodsMaxQty + 1)
    else : 
        setFoodQty(foodsMaxQty + 2)
        setFoodMaxQty(foodsMaxQty + 2)
    initFoods()
    
    clearPowerUps()
    initPowerUps()
    if numPlayer == 2 : setAlivePlayer(2)

def updatelevelText():
    levelText.clear()
    string = "Level : " + str(level) 
    levelText.write(string, align = "center", font = ("Arial", 24, "normal"))

def updateScoreText():
    string = "Score : " + str(score) + "      High Score : " + str(highScore)
    scoreText.clear()
    scoreText.write(string, align = "center", font = ("Arial", 24, "normal"))

def isCollideWithEnemy():
    if invincible == 1 : return False
    if numPlayer == 1 :
        for en in enemies:
            if isInRangeOfPoint(en.xcor(), en.ycor(), player.xcor(), player.ycor(), 10.0) : return True
        return False
    else :
        flag = 0
        for en in enemies:
            if isInRangeOfPoint(en.xcor(), en.ycor(), player.xcor(), player.ycor(), 10.0) : 
                flag += 1
                player.goto(-INVALID_CONSTANT,-INVALID_CONSTANT)
            if isInRangeOfPoint(en.xcor(), en.ycor(), player2.xcor(), player2.ycor(), 10.0) : 
                flag += 1
                player2.goto(-INVALID_CONSTANT,-INVALID_CONSTANT)
        if flag != 0 : 
            setAlivePlayer(alivePlayer-flag)
            if alivePlayer == 0 : return True
            else : return False
        return False

def isCollideWithFood():
    flag = False
    for i in range(foodsQty):
        if isInRangeOfPoint(foods[i].xcor(), foods[i].ycor(), player.xcor(), player.ycor(), 10.0): flag = True
        if numPlayer == 2 and isInRangeOfPoint(foods[i].xcor(), foods[i].ycor(), player2.xcor(), player2.ycor(), 10.0): flag = True
        
        if flag == True:
            foods[i].goto(INVALID_CONSTANT,INVALID_CONSTANT)
            foods.pop(i)
            setFoodQty(foodsQty - 1)
            return True
    return False        

def isCollideWithPowerUp():
    if numPlayer == 1 : 
        for i in range(powerUpsQty):
            if isInRangeOfPoint(powerUps[i].xcor(), powerUps[i].ycor(), player.xcor(), player.ycor(), 10.0):
                powerUps[i].goto(INVALID_CONSTANT,INVALID_CONSTANT)
                return i
        return -1
    else :
        for i in range(powerUpsQty):
            if isInRangeOfPoint(powerUps[i].xcor(), powerUps[i].ycor(), player.xcor(), player.ycor(), 10.0) or isInRangeOfPoint(powerUps[i].xcor(), powerUps[i].ycor(), player2.xcor(), player2.ycor(), 10.0):
                powerUps[i].goto(INVALID_CONSTANT,INVALID_CONSTANT)
                return i
        return -1

def getPowerUp(PUType):
    clearPowerUps()
    if PUType == 0:
        setLongDash(1)
        setPUTime(500)
        player.color("purple")
        if numPlayer == 2 : player2.color("purple")
    elif PUType == 1:
        setInvincible(1)
        setPUTime(500)
        player.color("grey")
        if numPlayer == 2 : player2.color("grey")
    elif PUType == 2:
        setThroughTheWall(1)
        setPUTime(500)
        player.color("white")
        if numPlayer == 2 : player2.color("white")
    elif PUType == 3:
        setReverse(1)
        setPUTime(500)
        player.color("red")
        if numPlayer == 2 : player2.color("red")
    elif PUType == 4:
        if alivePlayer == 1 and player.xcor() == -INVALID_CONSTANT and player.ycor() == -INVALID_CONSTANT : player.goto(-280,0)
        if alivePlayer == 1 and player2.xcor() == -INVALID_CONSTANT and player2.ycor() == -INVALID_CONSTANT : player2.goto(-280,0)
        setAlivePlayer(2)
        setPUTime(100)
        power.clear()
        textPower = "Back To Life"
        power.write(textPower, align = "center", font = ("Arial", 24, "normal"))
        winsound.PlaySound("mixkit-player-boost-recharging-2040.wav", winsound.SND_ASYNC)
        return 1
    power.clear()
    textPower = typePower[PUType] + "in 5.0 seconds"
    power.write(textPower, align = "center", font = ("Arial", 24, "normal"))
    winsound.PlaySound("mixkit-player-boost-recharging-2040.wav", winsound.SND_ASYNC)

def gameOver():
    power.clear()
    winsound.PlaySound("mixkit-player-losing-or-failing-2042.wav", winsound.SND_ASYNC)
    gameOverText.write("GAME OVER", align = "center", font = ("Arial", 24, "normal"))
    time.sleep(3)
    gameOverText.clear()
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
    if numPlayer == 2 : setAlivePlayer(2)

def registerShape():
    turtle.register_shape("powerUp.gif")
    turtle.register_shape("wall.gif")
    turtle.register_shape("enemy.gif")
    turtle.register_shape("energy.gif")

def readHighScore():
    file = open("highscore.txt", "rt")
    setHighScore(int(file.read()))
    file.close()

def saveHighScore():
    file = open("highscore.txt", "w")
    temp = highScore
    string = str(temp)
    file.write(string)
    file.close()

def setReverse(isActive):
    global reversedMove
    reversedMove = isActive

def deactivePU():
    setPUTime(0)
    setPUType(-1)
    setThroughTheWall(0)
    setInvincible(0)
    setLongDash(0)
    setReverse(0)
    setPUTime(0)
    player.color("aqua")
    if numPlayer == 2 : player2.color("aqua")

def PUTimer():
    if PUTime > 0:
        setPUTime(PUTime - 1)
        if PUTime <= 0 : 
            deactivePU()
            power.clear()
        elif PUTime % 100 == 0:
            power.clear()
            textPower = typePower[PUType]+"in "+str(PUTime/100)+" seconds"
            power.write(textPower, align = "center", font = ("Arial", 24, "normal"))
    
def pauseScreen():
    if isPaused : return 1
    setPaused(True)
    pause = turtle.Turtle()
    pause.speed(0)
    pause.color("white")
    pause.penup()
    pause.goto(0,0)
    
    countDown = 5
    
    for i in range(5, 0, -1):
        string = "Paused in " +  str(countDown) + " seconds"
        countDown -= 1
        pause.write(string, align = "center", font = ("Arial", 40, "normal"))
        time.sleep(1)
        pause.clear()
        
    # print("masuk")
    setPaused(False)

# ========= FUNCTIONS ========= #

if __name__ == "__main__":
    numPlayer = window.numinput("Player", "Number of player [1|2] :") 
    if numPlayer != 1 and numPlayer != 2 : window.bye()
    elif numPlayer == 1 : player2.hideturtle()
    elif numPlayer == 2 : 
        initPlayer2()
        setPowerUpQty(5)
    createText()
    registerShape()
    readHighScore()
    updateScoreText()
    border()
    initObstacles()
    initEnemies()
    initFoods()
    initPowerUps()
    window.listen()
    window.onkey(mUp, "w")
    window.onkey(mDown, "s")
    window.onkey(mLeft, "a")
    window.onkey(mRight, "d")
    if numPlayer == 2:
        window.onkey(mUp2, "Up")
        window.onkey(mDown2, "Down")
        window.onkey(mLeft2, "Left")
        window.onkey(mRight2, "Right")
    window.onkey(pauseScreen, "space")
    
    while True:
        
        window.update()
        moveEnemy()
        if isGoalAchieved() : goToNextLevel()
        if isCollideWithEnemy() : gameOver()
        if isCollideWithFood() :
            setScore(score + 10)
            if score >= highScore : setHighScore(int(score))
            updateScoreText()
        
        temp = isCollideWithPowerUp()   
        if temp >= 0 : 
            setPUType(temp)
            getPowerUp(temp)
            temp = -1
        PUTimer()
        time.sleep(DELAY)

    window.mainloop()