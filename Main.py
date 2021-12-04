import turtle
import time
import os

delay = 0.001

window = turtle.Screen()
window.title("Pac-Entre-Lagi")
window.bgcolor("black")
window.setup(width = 600, height = 600)
window.tracer(0)

player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("lightgreen")
player.penup()
player.goto(0,0)
player.direction = "stop"

# Functions #

def move_up():
    y = player.ycor()
    player.sety(y + 20)

def move_down():
    y = player.ycor()
    player.sety(y - 20)

def move_left():
    x = player.xcor()
    player.setx(x - 20)

def move_right():
    x = player.xcor()
    player.setx(x + 20)


# Keyboard 
window.listen()
window.onkey(move_up, "w")
window.onkey(move_down, "s")
window.onkey(move_left, "a")
window.onkey(move_right, "d")

while True:
    window.update()
    time.sleep(delay)
    
window.mainloop()
    