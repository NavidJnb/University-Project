import turtle
import random

screen = turtle.Screen()
screen.setup(800, 800)
screen.title("Coral - Chaos Game")
screen.bgcolor("white")
screen.tracer(0, 0) 

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()


x, y = 0, 0

n = 100000 

for _ in range(n):
    r = random.random()
    
    if r < 0.40:  
        new_x = 0.31 * x - 0.53 * y + 0.89
        new_y = -0.46 * x - 0.29 * y + 1.04
        color = "coral"
    elif r < 0.55: 
        new_x = 0.31 * x - 0.08 * y + 0.22
        new_y = 0.15 * x - 0.45 * y + 0.34
        color = "red"
    else:          
        new_x = 0.55 * y + 0.01
        new_y = 0.69 * x - 0.20 * y + 0.38
        color = "blue"
        
   
    x, y = new_x, new_y
    
    t.goto(x * 200, y * 200) 
    t.dot(2, color)          

screen.update()
turtle.done()

