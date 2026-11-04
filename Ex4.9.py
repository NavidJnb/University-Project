import turtle as t
import random

t.speed(999999900000000)
t.penup()
t.hideturtle()

x = 0
y = 0

for i in range(20000):
    r = random.random()

    if r < 0.02:
        new_x = 0
        new_y = 0.27 * y

    elif r < 0.17:
        new_x = -0.14 * x + 0.26 * y + 0.57
        new_y = 0.25 * x + 0.22 * y - 0.04

    elif r < 0.30:
        new_x = 0.17 * x - 0.21 * y + 0.41
        new_y = 0.22 * x + 0.18 * y + 0.09

    else:
        new_x = 0.78 * x + 0.03 * y + 0.11
        new_y = -0.03 * x + 0.74 * y + 0.27

    x = new_x
    y = new_y

    t.goto(x * 100, y * 100)
    t.dot(2, "green")

t.done()