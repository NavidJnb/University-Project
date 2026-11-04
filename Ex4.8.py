import turtle as t
import random

# مختصات رئوس مثلث
R = (-200, -150)
G = (200, -150)
B = (0, 196)

# رسم مثلث
t.speed(0)
t.penup()

for p in [R, G, B, R]:
    t.goto(p)
    t.pendown()

# شروع از رأس R
x, y = R

# رنگ هر رأس
vertices = [R, G, B]
colors = ["red", "green", "blue"]

# بازی آشوب
t.penup()

for i in range(5000):
    k = random.randint(0, 2)
    vx, vy = vertices[k]

    x = (x + vx) / 2
    y = (y + vy) / 2

    t.goto(x, y)
    t.dot(3, colors[k])

t.hideturtle()
t.done()