
 
#ترسیم یک مثلث

import turtle

def draw_triangle(x0, y0, x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x0, y0)
    turtle.pendown()

    turtle.goto(x1, y1)
    turtle.goto(x2, y2)
    turtle.goto(x0, y0)

    turtle.done()