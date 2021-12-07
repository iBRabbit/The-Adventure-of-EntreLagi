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

level = 1
score = 0
obsQty = DEFAULT_MAX_OBS
enemiesQty = DEFAULT_MAX_ENEMIES
foodsQty = DEFAULT_MAX_FOODS
foodsMaxQty = DEFAULT_MAX_FOODS

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
foods = []

# ========= INIT VARIABLES ========= #

# ========= SETTER ======== #
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
        ob.color("green")
        ob.shape("triangle")
        obs.append(ob)

def initEnemies():
    for i in range(enemiesQty):
        check = False
        while not check:
            posx = random.randint(-14, 14) * 20 
            posy = random.randint(-14, 14) * 20
            for j in range(obsQty):
                if abs(posx - obs[j].xcor()) >= 20 and abs(posy - obs[j].ycor()) >= 20:
                    check = True
                    break
            if check: break

        en = turtle.Turtle()
        en.speed = 1
        en.penup()
        en.setposition(posx, posy)
        en.color("red")
        en.shape("circle")
        direction = random.randint(1,4)
        if direction == 1 : en.direction = "Up"
        elif direction == 2 : en.direction = "Down"
        elif direction == 3 : en.direction = "Left"
        elif direction == 4 : en.direction = "Right"
        enemies.append(en)

def initFoods():
    for i in range(foodsQty):
        posx = random.randint(-14, 14) * 20 
        posy = random.randint(-14, 14) * 20
        
        while posx == -280 and posy == 0 or posx == 280 and posy == 0:
            posx = random.randint(-14, 14) * 20 
            posy = random.randint(-14, 14) * 20
        
        food = turtle.Turtle()
        food.speed = 0
        food.penup()
        food.goto(posx, posy)
        food.color("pink")
        food.shape("turtle")
        foods.append(food)
   

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
    if obstaclesCheck(x, y + 20) : return False
    if outOfMapLimit(x, y+20): return False
    player.sety(y + 20)

def moveDown():
    x,y = getPlayerCurrentPos()
    if obstaclesCheck(x, y - 20) : return False
    if outOfMapLimit(x, y-20): return False
    player.sety(y - 20)

def moveLeft():
    x,y = getPlayerCurrentPos()
    if obstaclesCheck(x - 20, y) : return False
    if outOfMapLimit(x-20, y): return False
    player.setx(x - 20)

def moveRight():
    x,y = getPlayerCurrentPos()
    if obstaclesCheck(x + 20, y) : return False
    if outOfMapLimit(x+20, y): return False
    player.setx(x + 20)

def isInRangeOfPoint(a,b,x,y,radius):
    if a >= x-radius and a <= x+radius and b >= y-radius and b <= y+radius:
        return True 
    return False

def obstaclesCheck(nextX, nextY):
    for i in range(obsQty):
        if isInRangeOfPoint(obs[i].xcor(), obs[i].ycor(), nextX, nextY, 10): return True
    return False


def checkEnemyMove(direction, posx, posy):
    if direction == "Up" or direction == "Down":
        if direction == "Up" and not obstaclesCheck(posx, posy+20) : return direction
        elif direction == "Down" and not obstaclesCheck(posx, posy-20) : return direction
        elif not obstaclesCheck(posx+20, posy) and obstaclesCheck(posx-20, posy): return "Right"
        elif obstaclesCheck(posx+20, posy) and not obstaclesCheck(posx-20, posy): return "Left"
        elif not obstaclesCheck(posx+20, posy) and not obstaclesCheck(posx-20, posy): 
            if distance(player.xcor(), player.ycor(), posx+20, posy) < distance(player.xcor(), player.ycor(), posx-20, posy): 
                return "Right"
            else: return "Left"
    elif direction == "Left" or direction == "Right":
        if direction == "Left" and not obstaclesCheck(posx-20, posy): return direction
        elif direction == "Right" and not obstaclesCheck(posx+20, posy): return direction
        elif not obstaclesCheck(posx, posy+20) and obstaclesCheck(posx, posy-20): return "Up"
        elif obstaclesCheck(posx, posy+20) and not obstaclesCheck(posx, posy-20): return "Down"
        elif not obstaclesCheck(posx, posy+20) and not obstaclesCheck(posx, posy-20): 
            if distance(player.xcor(), player.ycor(), posx, posy+20) < distance(player.xcor(), player.ycor(), posx, posy-20): 
                return "Up"
            else: return "Down"

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
    for ob in obs:
        ob.goto(9999999,9999999)
    
    for en in enemies:
        en.goto(9999999,9999999)
        
    for food in foods:
        food.goto(9999999,9999999)
    
    foods.clear()
    obs.clear()
    enemies.clear()     

def setPlayerToSpawn():
    player.setx(-280)
    player.sety(0)
    player.direction = "stop"

def isGoalAchieved():
    if player.distance(goal) < 20.0 and foodsQty <= 0: return True
    else : return False
        

def goToNextLevel():
    clearAll()
    setPlayerToSpawn()

    setLevel(level + 1)
    updatelevelText()
    
    setObstaclesQty(obsQty + 2)
    initObstacles()
    
    if level % 4 == 0 : setEnemiesQty(enemiesQty + 1)
    initEnemies()

    foodsMaxQty
    setFoodMaxQty(foodsMaxQty + 1)
    setFoodQty(foodsMaxQty + 1)
    initFoods()

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
        if isInRangeOfPoint(en.xcor(), en.ycor(), player.xcor(), player.ycor(), 20.0) : return True
    return False

def isCollideWithFood():
    for i in range(foodsQty):
        if isInRangeOfPoint(foods[i].xcor(), foods[i].ycor(), player.xcor(), player.ycor(), 20.0) : 
            foods[i].goto(-5000,5000)
            foods.pop(i)
            setFoodQty(foodsQty - 1)
            return True
    return False        

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
    gameOverText.write("GAME OVER", align = "center", font = ("Arial", 24, "normal"))
    time.sleep(3)
    gameOverText.clear()


# ========= FUNCTIONS ========= #

if __name__ == "__main__":
    border()
    initObstacles()
    initEnemies()
    initFoods()

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
        if isCollideWithEnemy() : gameOver()
        if isCollideWithFood():
            setScore(score + 10)
            updateScoreText()
        time.sleep(DELAY)

    window.mainloop()