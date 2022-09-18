from turtle import *

speed(0)
cell = 30
left(90)
for i in range(7):
    forward(10 * cell)
    right(120)

penup()
for x in range(0, 11 * cell, cell):
    for y in range(0, 11 * cell, cell):
        goto(x, y)
        dot(3)

done()