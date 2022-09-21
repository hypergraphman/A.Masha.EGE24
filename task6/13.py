from turtle import *

speed(0)
cell = 30
left(90)
forward(8 * cell)
for i in range(4):
    right(90)
    forward(4 * cell)

penup()
for x in range(0, 11 * cell, cell):
    for y in range(0, 11 * cell, cell):
        goto(x, y)
        dot(3)

done()