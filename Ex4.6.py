import turtle as t

t.speed(5)

# دایره سمت چپ
t.penup()
t.goto(-150, -100)
t.pendown()
t.circle(40)

# دایره سمت راست
t.penup()
t.goto(150, -100)
t.pendown()
t.circle(40)

# دایره بالایی
t.penup()
t.goto(0, 150)
t.pendown()
t.circle(40)

# اتصال سه نقطه
t.penup()
t.goto(-150, -60)
t.pendown()
t.goto(0, 190)
t.goto(150, -60)
t.goto(-150, -60)

t.done()



