import turtle as t 

from random import random

for i in range(100):
    step = int (random()*100)
    angle = int(random()*360)
    t.right(angle)
    t.fd(step)